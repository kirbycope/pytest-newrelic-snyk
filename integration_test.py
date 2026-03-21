import logging
import requests
import pytest


def test_000(config: dict):
    """ Test to verify that the configuration is loaded correctly and contains the expected values. """
    logging.info(f"Config: {config}")
    assert config["api_key"] is not None
    assert config["base_url"] is not None
    logging.info("Finished test_000")


@pytest.mark.positive
def test_001(config: dict):
    """ Test to verify that a GET request to a valid endpoint returns a 200 response. """
    logging.info(f"Config: {config}")
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    logging.info("Finished test_001")


@pytest.mark.negative
def test_002(config: dict):
    """ Test to verify that a GET request to an invalid endpoint returns a 404 response. """
    logging.info(f"Config: {config}")
    response = requests.get("https://jsonplaceholder.typicode.com/negative-endpoint")
    assert response.status_code == 404
    logging.info("Finished test_002")
