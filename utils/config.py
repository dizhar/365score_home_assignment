import os
from dotenv import load_dotenv

# Load .env file
loaded = load_dotenv()
print(f"🔹 .env file loaded: {loaded}")  # ✅ Check if dotenv successfully loaded

class Config:
    """Configuration settings for API testing."""

    # Base API URL
    BASE_URL = os.getenv("BASE_URL")
    REPORT_DIR = os.getenv("REPORT_DIR")
    MAX_RETRIES = os.getenv("MAX_RETRIES")
    LOG_FILE = os.getenv("LOG_FILE")

# Debugging: Print all loaded variables
print(f"🔹 BASE_URL: {Config.BASE_URL}")
print(f"🔹 REPORT_DIR: {Config.REPORT_DIR}")
print(f"🔹 MAX_RETRIES: {Config.MAX_RETRIES}")
print(f"🔹 LOG_FILE: {Config.LOG_FILE}")
