# pytest-newrelic-snyk
Sample Integration test using PyTest, logged by NewRelic, and secured by Snyk.

## Technologies Used
- [PyTest](https://docs.pytest.org/en/stable/) The PyTest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
- [Locust](https://locust.io/) An open source load testing tool. Define user behaviour with Python code, and swarm your system with millions of simultaneous users.
- [NewRelic](https://newrelic.com/) New Relic is an AI-powered observability platform that correlates your telemetry across your entire stack, so you can isolate the root cause and reduce MTTR.
- [Snyk](https://snyk.io/) Snyk is the AI Security Fabric. Secure at inception with continuous, autonomous defense for AI-generated code and AI-native apps.

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
   # Test Configuration
    API_KEY=1234567890abcdef
    BASE_URL=https://api.example.com

    # Locust Load Test Configuration
    MAX_FAIL_RATIO=0.01
    MAX_AVG_RESPONSE_TIME=500
    MAX_RESPONSE_TIME_PERCENTILE=2000
   ```
    1. These will be used by [/conftest.py](/conftest.py) and [/locustfile.py](/locustfile.py)

## [As-needed] Update Installed Packages
1. Open [/requirements.txt](/requirements.txt)
1. Find and replace: `==` with `>=`
    - "==" is used to lock the version so that CI does not use untested versions
1. With `(.venv)` active, update the packages: `pip install --upgrade -r requirements.txt`
1. Then lock the versions again: `pip freeze > requirements.txt`

----

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

# [One-time] Locust GitHub Action Setup
1. Navigate to https://github.com/kirbycope/pytest-newrelic-snyk/settings/variables/actions
    - Optionally, you could save this as an organization variable if available for your account
1. Select the "New repository variable" button
1. Enter the name `MAX_FAIL_RATIO` and the `0.01`, then select the "Add variable" button
1. Select the "New repository variable" button
1. Enter the name `MAX_AVG_RESPONSE_TIME` and the `500`, then select the "Add variable" button
1. Select the "New repository variable" button
1. Enter the name `MAX_RESPONSE_TIME_PERCENTILE` and the `2000`, then select the "Add variable" button
    - This is the "timeout" for P95 responses

## [One-time] NewRelic GitHub Action Setup
1. Navigate to https://one.newrelic.com/admin-portal/api-keys/home
1. Select the "Create a key" button
1. Change the "Key type" to "Ingest - License"
1. Name the key: `License Key for GitHub Actions`
1. Enter the Notes: `Used to upload GHA results to NewRelic`
1. Select the "Create a key" button
1. Select the "Copy key" button
1. Navigate to https://github.com/kirbycope/pytest-newrelic-snyk/settings/secrets/actions
    - Optionally, you could save this as an organization secret if available for your account
1. Select the "New repository secret" button
1. Enter the name `NEW_RELIC_LICENSE_KEY` and the key ID, then select the "Add secret" button

## [One-time] NewRelic Dashboard Setup
1. Navigate to https://one.newrelic.com/dashboards
1. Select the "Create a dashboard" button
1. Select the "Create a new dashboard" button
1. Name the dashboard and then select "Create"
1. Select the dashboard from the table

## [One-time] Snyk GitHub Action Setup
1. Navigate to https://app.snyk.io/org/kirbycope/manage/snyk-code and verify "Enable Snyk Code" is enabled
1. Navigate to https://app.snyk.io/account/personal-access-tokens
1. Enter the Name: `PAT for GitHub Actions`
1. For Expiry, select "6 months"
    - Enterprise users should use a Service Account API Token
1. Select the "Generate new token" button
    1. Copy the Personal Access Token
    1. Navigate to https://github.com/kirbycope/pytest-newrelic-snyk/settings/secrets/actions
    1. Select the "New repository secret" button
    1. Enter the name `SNYK_TOKEN` and the PAT value, then select the "Add secret" button
1. Navigate to https://app.snyk.io/org/kirbycope/manage/settings
    1. Copy the Organization ID
    1. Navigate to https://github.com/kirbycope/pytest-newrelic-snyk/settings/variables/actions
    1. Select the "New repository variable" button
    1. Enter the name `SNYK_ORG_ID` and the Organization ID value, then select the "Add variable" button 

### Create the Column Header
1. Select the "+ Add widget" button
1. Select the "Add text, images, links, or diagrams" button
1. Edit the text to: `# ![Alt text](https://docs.pytest.org/en/stable/_static/favicon.png) PyTest Integration Tests` and then select the "Save" button
1. Use the ellipsis ("...") button to duplicate and edit additional headers

### Create a Pass/Fail Widget
1. Select the "+ Add widget" button
1. Select the "Add a chart" button
1. Paste in the following:
    ```
    FROM Span
    SELECT latest(conclusion) = 'success' as 'Success', latest(timestamp)
    WHERE entity.name = 'kirbycope/pytest-newrelic-snyk'
    AND name = 'PyTest'
    SINCE last month
    ```
1. Select the "Run" button
1. Under "Basic Information":
    1. Set "Name": `pytest-newrelic-snyk Integration Tests`
    1. Set "URL": `https://github.com/kirbycope/pytest-newrelic-snyk/actions/workflows/integration.yml`
    1. Set "Description": `PyTest`
1. Under "Thresholds":
    1. Add: "From": `0`, "To": `0`, and "Severity level": "Critical"
    1. Add: "From": `1`, "To": `1`, and "Severity level": "Good"
1. Under "Data Format"
    1. Attribute: "timestamp"
    1. Type: "Date / time"
    1. Format: "Select a format"
1. Dashboard options:
    1. Ignore time picker: "true"
1. Billboard settings:
    1. Display mode: "Value and label"
    1. Alignment: "Stacked (default)"
    1. Columns amount: `1`
1. (Optional) Add link:
    1. Title: `See results on GitHub`
    1. Url: `https://github.com/kirbycope/pytest-newrelic-snyk/actions/workflows/integration.yml`
    1. Open in a new tab: "true"
1. Select the "Apply changes" button
1. Use the ellipsis ("...") button to duplicate and edit additional widgets
