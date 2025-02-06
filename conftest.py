import os
import pytest
import logging
from utils.api_client import APIClient
from utils.config import Config  # ✅ Import Config

# Ensure the report directory exists
REPORT_DIR = Config.REPORT_DIR or "Report/"  # ✅ Default fallback
if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)
    print(f"✅ Created Report Directory: {REPORT_DIR}")
else:
    print(f"✅ Report Directory Already Exists: {REPORT_DIR}")

# Configure pytest to use dynamic Allure directory
def pytest_configure(config):
    """Set pytest options dynamically based on .env configuration"""
    config.option.allure_report_dir = REPORT_DIR
    print(f"📁 Allure reports will be stored in: {REPORT_DIR}")

# Configure logging for pytest
@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Sets up logging for tests."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.fixture(scope="session")
def api_client():
    """Fixture for API Client instance. Reused across all tests."""
    return APIClient()
