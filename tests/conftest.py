"""
Pytest configuration and shared fixtures for BlackHalo tests.
"""

import sys
from pathlib import Path

# Add project root to Python path so tests can import project modules
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# Shared fixtures can be added here
# Example:
# @pytest.fixture
# def sample_address():
#     return "BM-2cTux3PGRqHTEH6wyUP2sWeT4LrsGgy63z"
