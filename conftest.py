import os
import tempfile
import pytest
import pytest_html

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from APIUtils.AdminAPIs.UserAPIs import UserAPIs
from APIUtils.PIMAPIs.EmployeeAPIs import EmployeeApis
from BaseUtils.Dataset import Dataset
from PageFragments.LoginPageFragments.LoginPage import LoginPage
from _Wrapper.BaseClass import BaseClass
from OrangeHRMData.Constants import Constants
from _Wrapper.Paths import Paths


@pytest.fixture
def base_url(request):
    env = request.config.getoption("--environment")
    if env == "dev":
        return os.getenv("dev_env")
    elif env == "stage":
        return os.getenv("stage_env")
    elif env == "prod":
        return os.getenv("prod_env")
    else:
        # Default to the below url if no environment specified
        return os.getenv('default_env')


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--environment", action="store", default=None)  # Default environment is Open source


@pytest.fixture(scope="function", autouse=True)
def driver_fixture(request, base_url):
    browser_name = request.config.getoption("browser_name").lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Invalid browser name: {browser_name}")

    # Set the driver in the BaseFragment class
    BaseClass().set_driver(driver)
    BaseClass().set_base_url(base_url)
    BaseClass().navigate_to_url()
    yield driver  # Return the driver instance

    # Tear down after the test
    BaseClass().quit_browser()


@pytest.fixture(autouse=True)
def login(request, driver_fixture):
    if request.node.name.startswith("test_custom_user"):
        test_data = Dataset()
        # Creating an employee.
        emp_num = EmployeeApis().create_employee(last_name=test_data.last_name, first_name=test_data.first_name,
                                                 employee_id=test_data.emp_id)
        # Creating a user with the created employee.
        UserAPIs().create_user(username=test_data.user_name, password=test_data.password, empNumber=emp_num)
        username = test_data.user_name
        password = test_data.password
    else:
        username = os.getenv("admin_username")
        password = os.getenv("admin_password")

    wait = WebDriverWait(driver_fixture, timeout=Constants.short_live_throttle)  # Wait for a maximum of 10 seconds
    try:
        # Wait until the element is present on the page
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

        # Now, perform actions on the element
        LoginPage().run_login(username, password)

        # Use logger from BaseClass
        BaseClass().logger.info(f"Login successful for user: {username}")

        yield  # This allows the test to run after login

    except Exception as e:
        # Log the error
        BaseClass().logger.error(f"Login successful for user: {username}")
        # Print the error for visibility
        print(f"An error occurred: {e}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' and report.failed:
        # Get the test name from the item

        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            test_name = item.name

            # Take a screenshot using the BaseClass method
            screenshot_path = BaseClass.take_screenshot(test_name)

            base_folder = os.path.join(tempfile.gettempdir(), 'OrgHRM_Automation_Tests_Screenshot')
            os.makedirs(base_folder, exist_ok=True)

            # Use the screenshot path from the take_screenshot method

            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            extra.append(pytest_html.extras.image(screenshot_path))

        # ... (other code)

        report.extra = extra
