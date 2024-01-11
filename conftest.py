import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _Wrapper.BaseClass import BaseClass
from OrangeHRMData.Constants import Constants

base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php'
bearer = os.environ.get("ORANGEHRM_BEARER_TOKEN", "")


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
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
    BaseClass.set_driver(driver)
    BaseClass.navigate_to_url(base_url)
    yield driver  # Return the driver instance

    # Tear down after the test
    BaseClass.quit_browser()


@pytest.fixture
def admin_login(driver):
    username = "Admin"
    password = "admin123"

    wait = WebDriverWait(driver, timeout=Constants.short_live_throttle)  # Wait for a maximum of 10 seconds
    try:
        # Wait until the element is present on the page
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

        # Now, perform actions on the element
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        yield  # This allows the test to run after login

    except Exception as e:
        print(f"An error occurred: {e}")
