from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    dashboard_cards = (By.XPATH, "//div[contains(@class,'orangehrm-dashboard-widget-body')]")
    gear_icon = (By.XPATH, "//div[contains(@class,'emp-leave-chart')]//i")
    emp_leave_card = (By.XPATH, "//div[contains(@class,'emp-leave-chart')]")

    def all_cards(self):
        return self.driver.find_elements(*DashboardPage.dashboard_cards)

    def emp_leave_card_gear_btn(self):
        return self.driver.find_element(*DashboardPage.gear_icon)
