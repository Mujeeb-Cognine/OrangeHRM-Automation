import pytest

from selenium.webdriver.remote.webdriver import WebDriver

from _Wrapper.DefaultLogger import DefaultLog


@pytest.mark.usefixtures("driver")
class DriverInitialization:
    # Class variable to store the driver
    driver = None
    logger = DefaultLog.get()

    @classmethod
    def set_driver(cls, driver: WebDriver):
        if not isinstance(driver, WebDriver):
            raise TypeError("Invalid driver type. Must be an instance of WebDriver.")
        cls.driver = driver
