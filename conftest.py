import os
import pytest
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
def driver(request, base_url):
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
def login(request, driver):
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

    wait = WebDriverWait(driver, timeout=Constants.short_live_throttle)  # Wait for a maximum of 10 seconds
    try:
        # Wait until the element is present on the page
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

        # Now, perform actions on the element
        LoginPage().run_login(username, password)
        # driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
        # driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        # driver.find_element(By.XPATH, "//button[@type='submit']").click()
        yield  # This allows the test to run after login

    except Exception as e:
        print(f"An error occurred: {e}")
