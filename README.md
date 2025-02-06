Here's a clean and structured `README.md` for your **Pytest API Testing Boilerplate**:

---

# 🚀 Pytest API Testing Boilerplate

This repository provides a **simple and scalable boilerplate** for API testing using **Pytest**, **Allure Reports**, and **Logging**.

## 📌 Features

✅ **Pytest Framework** – Core testing framework  
✅ **Allure Reporting** – Beautiful and interactive test reports  
✅ **Retry Mechanism** – Auto-retry failed tests  
✅ **Logging** – Captures request and response details  
✅ **Structured API Client** – Handles API requests

---

## 🏗 Project Structure

```
pytest-boilerplate/
│── tests/
│   |── data
|   |     |── test_data.csv
├── test_users.py
│   ├── test_posts.py
│   ├── test_create_post.py
│── utils/
│   ├── api_client.py
│   ├── logger.py
│   ├── config.py
│── conftest.py
│── requirements.txt
│── .gitignore
│── pytest.ini
│── README.md
│── Report/
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dizhar/365score_home_assignment.git
cd 365score_home_assignment
```

### 2️⃣ Install Allure (Required for Reports)

Before running the tests, install Allure based on your OS:

📌 **Install Allure on macOS:**

```bash
brew install allure
```

📌 **Install Allure on Ubuntu/Debian:**

```bash
sudo apt install allure
```

📌 **Install Allure on Windows**  
Download and install Allure from the [official website](https://docs.qameta.io/allure/#_installing_a_commandline) or use [Scoop](https://scoop.sh/):

```bash
scoop install allure
```

### 2️⃣ Run the Setup Script

````bash
chmod +x setup.sh  # Make it executable (only needed once)
./setup.sh         # Run setup

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
````

---

## 📌 Running Tests

### Run all tests

```bash
pytest
```

### Run tests with Allure Reports

```bash
pytest
allure serve Report/
```

---

## 🎯 Configuration (`pytest.ini`)

```ini
[pytest]
addopts = --alluredir=Report/ --reruns 2 --reruns-delay 2
```

✔ Generates **Allure Reports**  
✔ Retries failed tests **twice**

---
