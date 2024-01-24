import pytest

from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("driver_fixture")
class DriverInitialization:
    # Class variable to store the driver
    driver = None

    @classmethod
    def set_driver(cls, driver: WebDriver):
        if not isinstance(driver, WebDriver):
            raise TypeError("Invalid driver type. Must be an instance of WebDriver.")
        cls.driver = driver
