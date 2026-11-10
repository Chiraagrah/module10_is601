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

View the Docker Hub repository for [`choreazam/601_module10`](https://hub.docker.com/r/choreazam/601_module10)

# Development and Deployment Challenges & Resolutions

## 1. Security Vulnerabilities & CI/CD Pipeline (Trivy)

* **Challenge:** 
  GitHub Actions security scans failed due to high-severity vulnerabilities from outdated Python dependencies and accidental inclusion of local virtual environments in the Docker build context.

* **Resolution:** 
  * Excluded virtual environments and generated artifacts using `.dockerignore`.
  * Upgraded vulnerable dependencies, including `dnspython` and FastAPI/Starlette (which also required updating template response calls in `main.py`).
  * Migrated the multi-stage Docker build and CI runtime to Python 3.11.

* **Outcome:** 
  Passed all Trivy security gates, with the full test suite (74 tests) and container tests (71 tests) passing successfully.

---

## 2. Database Initialization (Docker Compose & PostgreSQL)

* **Challenge:** 
  PostgreSQL startup failures during local container orchestration.

* **Resolution:** 
  * Pinned the database image to `postgres:18` and updated the data mount path to `/var/lib/postgresql`.
  * Created a fresh volume (`postgres_data_v18`) while leaving the legacy volume untouched.
  * Removed the obsolete Compose version field and validated the schema using `docker compose config`.