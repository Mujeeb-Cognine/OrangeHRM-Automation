from selenium.webdriver.common.by import By

from BaseUtils.BaseClass import BaseClass
from PageFragments.BasePageFragments import BasePageFragments


class DashboardPage(BasePageFragments):

    def __init__(self):
        BaseClass.__init__(self)

    dashboard_cards = (By.XPATH, "//div[contains(@class,'orangehrm-dashboard-widget-body')]")
    gear_icon = (By.XPATH, "//div[contains(@class,'emp-leave-chart')]//i")
    emp_leave_card = (By.XPATH, "//div[contains(@class,'emp-leave-chart')]")

    def all_cards(self):
        return self.driver.find_elements(*DashboardPage.dashboard_cards)

    def emp_leave_card_gear_btn(self):
        return self.driver.find_element(*DashboardPage.gear_icon)
