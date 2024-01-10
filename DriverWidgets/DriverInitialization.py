from selenium.webdriver.remote.webdriver import WebDriver


class DriverInitialization:
    driver = None  # Class variable to store the driver

    @classmethod
    def set_driver(cls, driver: WebDriver):
        cls.driver = driver
