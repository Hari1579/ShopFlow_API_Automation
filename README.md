# ShopFlow API Automation Framework

## Overview
**ShopFlow API Automation** is a scalable, enterprise-grade REST API testing framework built with Python and PyTest. It is designed to validate the reliability, performance, and schema compliance of the ShopFlow API services seamlessly through automated testing and continuous integration pipelines.

---

## Tech Stack
- **Language:** Python 3.x
- **Testing Framework:** PyTest
- **HTTP Client:** Requests
- **CI/CD Pipeline:** GitHub Actions
- **Reporting:** PyTest-HTML / Allure

---

## Key Features
- **JSON Schema Validation:** Ensures API responses strictly comply with defined structural contracts and data types.
- **Custom Logging System:** Provides clear, structured execution logs for rapid debugging and detailed audit trails.
- **CSV Data-Driven Testing:** Enables parameterized testing with dynamic test datasets managed via CSV files.
- **Interactive HTML Reports:** Generates detailed visual reports after test execution containing execution summaries and failures.

---

## Directory Structure
```
ShopFlow_API_Automation/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD workflows
├── config/                  # Environment & API configuration files
├── reports/                 # Test execution HTML reports & logs
├── test_data/               # CSV files for data-driven test cases
├── tests/
│   └── api/                # API test modules and scenarios
├── utils/                   # Helpers, loggers, schema validators, request wrappers
├── .gitignore               # Git ignore file rules
├── conftest.py              # PyTest fixtures and global hooks
├── pytest.ini               # PyTest configuration settings
└── requirements.txt         # Project dependencies
```

---

## How to Run Tests

### 1. Prerequisites
Ensure Python 3.8+ and `pip` are installed on your system.

### 2. Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/Hari1579/ShopFlow_API_Automation.git
cd ShopFlow_API_Automation
pip install -r requirements.txt
```

### 3. Execution Commands
Run all API tests:
```bash
pytest
```

Run tests with HTML report generation:
```bash
pytest --html=reports/report.html --self-contained-html
```

---

## CI/CD Workflow
The project leverages **GitHub Actions** for continuous integration:
- Automated execution triggered on `push` and `pull_request` events to the `main` branch.
- Automated secret injection for secure environment credentials.
- Test execution output captured and published directly as downloadable build artifacts (HTML Reports).
