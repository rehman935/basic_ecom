import os
import time
import re
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture( scope="function" )
def browser_instance(request):
    global driver
    browser_name = request.config.getoption( "browser_name" )
    service_obj = Service()
    if browser_name == "chrome":  #firefox
        driver = webdriver.Chrome( service=service_obj )
    elif browser_name == "firefox":
        driver = webdriver.Firefox( service=service_obj )

    driver.implicitly_wait( 5 )
    driver.get( "https://rahulshettyacademy.com/loginpagePractise/" )
    yield driver  #Before test function execution
    time.sleep(3)
    driver.close()  #post your test function execution


def sanitize_filename(name):
    """Sanitize test nodeid into a safe, flat filename."""
    return re.sub(r'[\\/*?:"<>|\[\]/]', '_', name)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ('call', 'setup'):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # ✅ Always save to the same directory as report.html
            report_dir = os.path.join(os.path.dirname(__file__), 'reports')
            os.makedirs(report_dir, exist_ok=True)

            # ✅ Flatten filename to avoid nested folders
            test_name = sanitize_filename(report.nodeid)
            screenshot_filename = f"{test_name}.png"
            screenshot_path = os.path.join(report_dir, screenshot_filename)

            # ✅ Take screenshot
            _capture_screenshot(screenshot_path)

            # ✅ Embed using relative path (just the filename)
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                html = (
                    f'<div><img src="{screenshot_filename}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

        report.extra = extra

def _capture_screenshot(file_path):
    try:
        global driver  # Ensure this is your actual WebDriver instance
        driver.get_screenshot_as_file(file_path)
        print("✅ Screenshot saved:", file_path)
    except Exception as e:
        print("❌ Screenshot failed:", e)

