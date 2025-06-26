
# Pytest-Selenium Test Automation Framework 🚀

This is a basic yet extensible test automation framework built using:

- 🧪 **Pytest** for test structure and execution  
- 🌐 **Selenium WebDriver** for browser automation  
- 📝 **pytest-html** for rich HTML reports  
- 🧩 Supports multiple browsers: Chrome and Firefox  
- 📸 Takes screenshots on test failure and embeds them in HTML reports  
- 📂 Easy command-line configuration via `--browser_name`
- ## 📁 Project Structure

inital_setup_for_pytest_framwork/
├── pytest.ini # Pytest configuration file
├── set_environment_pytest/
│ ├── conftest.py # Fixtures, hooks, browser setup
│ ├── test_e2e.py # Sample test
│ ├── test_sortTable.py # Another sample test
│ ├── test_e2etesting.py # More tests
│ ├── reports/ # HTML reports and screenshots
│ │ ├── report.html # Generated HTML test report
│ │ └── *.png # Screenshots of failed tests

## ✅ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/pytest-selenium-framework.git
cd pytest-selenium-framework
2 Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
3 Install dependencies
pip install -r requirements.txt
Make sure to install:
selenium
pytest
pytest-html

How to Run Tests
pytest set_environment_pytest/test_e2e.py

Run with HTML report and specific browser
pytest set_environment_pytest/test_e2e.py --browser_name=chrome --html=set_environment_pytest/reports/report.html

Supported Browsers
You can run tests using:

--browser_name=chrome

--browser_name=firefox

Example:
pytest --browser_name=firefox
Default is Chrome if nothing is specified.
