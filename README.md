# pytest-newrelic-snyk
Sample Integration test using PyTest, logged by NewRelic, and secured by Snyk.

## Technologies Used
- [PyTest](https://docs.pytest.org/en/stable/) The PyTest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
- [NewRelic](https://newrelic.com/) Intelligent Observability resolves issues at scale—before they impact your bottom line.
- [Snyk](https://snyk.io/) A new autonomous defense architecture designed for an era where code creation has accelerated beyond human capacity. Weave an invisible, intelligent layer of defense into every creation.

## Project Setup
1. Clone _this_ repo: `git clone https://github.com/kirbycope/pytest-newrelic-snyk.git`
1. Open the root directory: `cd pytest-newrelic-snyk`
1. Create a Virtual Environment for Python: `python -m venv .venv`
1. Activate the Virtual Environment:
    - [linux/macOS] `source .venv/bin/activate`
    - [Windows] `source .venv/Scripts/activate`
1. Verify Virtual Environment: `python --version`
    - It should respond with your Python version and `(.venv)`
1. To create the [/requirements.txt](/requirements.txt):
    1. `pip install --upgrade locust`
        - https://docs.locust.io/en/stable/ for load tests
    1. `pip install --upgrade pytest`
        - https://docs.pytest.org/en/stable/ for integration tests
    1. `pip install --upgrade pytest-html`
        - https://pytest-html.readthedocs.io/en/latest/ for test reports
    1. `pip install --upgrade pytest-retry`
        - https://github.com/str0zzapreti/pytest-retry for retrying flaky test
    1. `pip install --upgrade pytest-xdist`
        - https://pytest-xdist.readthedocs.io/en/stable/ for parallel test distribution
    1. `pip install --upgrade pytest-xdist[psutil]`
        - https://pytest-xdist.readthedocs.io/en/stable/ for CPU detection
    1. `pip install --upgrade python-dotenv`
        - https://github.com/theskumar/python-dotenv for loading secrets from a `.env` file or from the [os](https://docs.python.org/3/library/os.html).
    1. `pip freeze > requirements.txt`
1. Create a new file: `.env`
1. Edit the file to contain:
   ```
   API_KEY=1234567890abcdef
   BASE_URL=https://api.example.com
   ```
    1. These will be used by [/conftest.py](/conftest.py)

## [One-time] GitHub Environment Setup
1. Navigate to https://github.com/kirbycope/pytest-newrelic-snyk/settings/environments
1. Select the "New environment" button
1. Enter the name `Test` and then select the "Configure environment button"
1. Select the "Add environment secret" button
1. Enter the name `API_KEY` and its value (see `.env` above), then select the "Add secret" button
    - The API_Key is a secret. Keep it hidden, keep it safe!
1. Select the "Add environment variable" button
1. Enter the name `BASE_URL` and its value (see `.env` above), then select the "Add variable" button
    - While not a secret, this value changes based on the Environment under test

## Update Installed Packages
1. Open [/requirements.txt](/requirements.txt)
1. Find and replace: `==` with `>=`
    - "==" is used to lock the version so that CI does not use untested versions
1. With `(.venv)` active, update the packages: `pip install --upgrade -r requirements.txt`
1. Then lock the versions again: `pip freeze > requirements.txt`
