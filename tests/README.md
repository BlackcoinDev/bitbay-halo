# BlackHalo Test Suite

This directory contains the test suite and code quality tools for the BlackHalo project.

## Structure

```
tests/
├── scripts/
│   ├── lint.py       # Check style issues
│   └── format.py     # Auto-format code
├── conftest.py       # Pytest fixtures
├── test_addresses.py # Address encoding tests
├── test_crypto.py    # Cryptographic tests
└── README.md
```

## Quick Commands

| Command | Purpose |
|---|---|
| `uv run python tests/scripts/lint.py` | Check style issues |
| `uv run python tests/scripts/format.py` | Auto-format code |
| `uv run pytest` | Run tests with coverage |
| `uv run pytest --cov-report=html` | Generate HTML coverage report |

## Setup

```bash
# Create venv with uv
uv venv venv --python 3.14
source venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Install dev tools
uv pip install pytest flake8 black isort
```
