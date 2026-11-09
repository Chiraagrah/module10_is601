# Running Tests Locally

Install the project dependencies and activate your virtual environment, then run
the test suite from the repository root:

```bash
pip install -r requirements.txt
python -m pytest
```

To run a specific test group:

```bash
python -m pytest tests/unit/
python -m pytest tests/integration/
python -m pytest tests/e2e/
```

End-to-end tests use Playwright. Install its Chromium browser before running
them:

```bash
playwright install chromium
```

Tests use an isolated in-memory SQLite database by default. To use a persistent
test database, set `TEST_DATABASE_URL` before running pytest. Test fixtures drop
and recreate tables, so use a dedicated test database.

# Docker Hub

[View the Docker Hub repository for `choreazam/601_module10`](https://hub.docker.com/r/choreazam/601_module10)
