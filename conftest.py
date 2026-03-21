import os
import pytest

from dotenv import load_dotenv
load_dotenv()


@pytest.fixture(scope="session")
def config(request: pytest.FixtureRequest) -> dict:
    """
    Load configuration from environment variables and provide it as a fixture for tests.

    This fixture is scoped to the entire test session, meaning it will be created once and shared across all tests.
    It retrieves configuration values from environment variables, which can be set in a .env file or directly in the environment.

    Returns:
        dict: A dictionary containing configuration values for the tests.
    """
    config = {
        "api_key": os.getenv("API_KEY"),
        "base_url": os.getenv("BASE_URL"),
    }
    return config
