import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DefaultData.OrangeHRMData import TimeoutConstants


@pytest.mark.usefixtures("driver")
class BaseClass:

    def verify_element_presence(self, driver: WebDriver, element_locator):
        try:
            WebDriverWait(driver, timeout=TimeoutConstants.default).until(
                EC.presence_of_element_located(element_locator))
            return True
        except:
            return False
