#!/bin/bash

# Set strict mode for error handling
set -e

echo "🔹 Checking if Python 3.9 is installed..."
if ! command -v python3.9 &> /dev/null
then
    echo "❌ Python 3.9 not found! Installing..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS Installation
        brew install python@3.9
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux Installation
        sudo apt update && sudo apt install -y python3.9 python3.9-venv
    else
        echo "❌ Unsupported OS. Please install Python 3.9 manually."
        exit 1
    fi
else
    echo "✅ Python 3.9 is installed."
fi

# Remove old virtual environment
echo "🔹 Removing old virtual environment..."
rm -rf venv    

# Create a new virtual environment using Python 3.9
echo "🔹 Creating a new virtual environment..."
python3.9 -m venv venv

# Activate the virtual environment
echo "🔹 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip to the latest version
echo "🔹 Upgrading pip..."
pip install --upgrade pip

# Ensure no conflicting packages exist
echo "🔹 Removing conflicting packages..."
pip uninstall -y pytest-allure-adaptor allure allure-pytest allure-python-commons || true

# Verify if pytest-allure-adaptor is truly removed
echo "🔹 Verifying that pytest-allure-adaptor is fully uninstalled..."
while pip list | grep -q "pytest-allure-adaptor"; do
    echo "❌ pytest-allure-adaptor is still installed! Force removing..."
    pip uninstall -y pytest-allure-adaptor
done
echo "✅ pytest-allure-adaptor is removed."

# Check what package is trying to reinstall pytest-allure-adaptor
echo "🔹 Checking which package requires pytest-allure-adaptor..."
pipdeptree | grep -B1 "pytest-allure-adaptor" || echo "✅ No dependencies require pytest-allure-adaptor."

# Clear pip cache to remove any cached installations
echo "🔹 Clearing pip cache..."
pip cache purge

# Install required dependencies
echo "🔹 Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Ensure pytest-allure-adaptor is STILL NOT installed
if pip list | grep -q "pytest-allure-adaptor"; then
    echo "❌ pytest-allure-adaptor was reinstalled! Trying to remove it again..."
    pip uninstall -y pytest-allure-adaptor
else
    echo "✅ pytest-allure-adaptor did NOT return. Good!"
fi

# Reinstall the correct allure-pytest version
echo "🔹 Installing allure-pytest..."
pip install --upgrade allure-pytest allure-python-commons

# Verify if allure.severity_level exists
echo "🔹 Verifying Allure installation..."
if python -c "import allure; print(hasattr(allure, 'severity_level'))" | grep -q "True"; then
    echo "✅ allure.severity_level exists."
else
    echo "❌ Error: allure.severity_level missing. Reinstalling allure-pytest..."
    pip install --force-reinstall allure-pytest allure-python-commons
fi

# Check if pytest detects allure-pytest
echo "🔹 Checking if pytest detects allure-pytest..."
pytest --trace-config | grep "allure-pytest" || echo "❌ pytest does not detect allure-pytest. Something is wrong."

echo "✅ Setup complete! You can now run pytest with allure."
