import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DefaultData.OrangeHRMData import TimeoutConstants

base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php'
bearer = ("Bearer def502001f64fdfdc63165f8f62269dba1e133d0727e6ef8c84b9ce32ca18ee0a9f05f7f63f3704af82ed481dcf76956ea382"
          "fabf8b66a5668e94d190071d6d1d2e1eed28ac86645eb6d4b0900efcf6e5da9e9dfd87527a2b2da77019089b3be8a2cc8a8f9ff073f8"
          "a64933cc54967ce440462c01142766f071771d19fcd37015cb6de198df5be6ed000fd6ef1408f32641769d8746d3539cd52c8b53c3ea"
          "442fafafce0")


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

    driver.get(base_url)
    driver.maximize_window()
    yield driver  # Return the driver instance

    # Tear down after the test
    driver.close()


@pytest.fixture
def admin_login(driver):
    username = "Admin"
    password = "admin123"

    wait = WebDriverWait(driver, timeout=TimeoutConstants.default)  # Wait for a maximum of 10 seconds
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
