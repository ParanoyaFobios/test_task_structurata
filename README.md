# Test Task for Structurata

Client for JSONPlaceholder API with Service Layer and In-Memory Storage.

## Stack
- Python 3.12
- UV (Package Manager)
- Requests
- Wemake-python-styleguide (Linter)
- Mypy (Type Checking)
- Pytest

## How to run
1. Install dependencies: `uv sync`
2. Run app: `uv run python main.py`
3. Run linter: `uv run flake8 .`
4. Run tests: `uv run python -m pytest`