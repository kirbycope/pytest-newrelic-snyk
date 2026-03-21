import logging
import os
from locust import HttpUser, task, between, events

from dotenv import load_dotenv
load_dotenv()

config = {
    "api_key": os.getenv("API_KEY"),
    "base_url": os.getenv("BASE_URL"),

    "max_fail_ratio": float(os.getenv("MAX_FAIL_RATIO", 0.01)),
    "max_avg_response_time": float(os.getenv("MAX_AVG_RESPONSE_TIME", 200)),
    "max_response_time_percentile": float(os.getenv("MAX_RESPONSE_TIME_PERCENTILE", 800)),
}

@events.quitting.add_listener
def _(environment, **kw):
    """ https://docs.locust.io/en/1.6.0/running-locust-without-web-ui.html#controlling-the-exit-code-of-the-locust-process """
    if environment.stats.total.fail_ratio > config["max_fail_ratio"]:
        logging.error(f"Test failed due to failure ratio > {config['max_fail_ratio'] * 100}%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > config["max_avg_response_time"]:
        logging.error(f"Test failed due to average response time > {config['max_avg_response_time']} ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > config["max_response_time_percentile"]:
        logging.error(f"Test failed due to 95th percentile response time > {config['max_response_time_percentile']} ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0

class APIUser(HttpUser):
    wait_time = between(1, 5)
    host = config["base_url"]

    def on_start(self) -> None:
        self.client.headers = {
            "x-api-key": config['api_key']
        }

    @task
    def test_001(self):
        """ Task to verify that a GET request to a valid endpoint returns a 200 response. """
        self.client.get(
            url = "/posts/1",
            name = "GET /posts/1",
        )
