from selenium.webdriver.common.by import By

from _Wrapper.BaseClass import BaseClass
from PageFragments.BasePageFragments import BasePageFragments


class DashboardPage(BasePageFragments):

    def __init__(self):
        BaseClass.__init__(self)

    dashboard_cards = "//div[contains(@class,'orangehrm-dashboard-widget-body')]"
    employee_leave_card_gear_icon = "//div[contains(@class,'emp-leave-chart')]//i"
    emp_leave_card = "//div[contains(@class,'emp-leave-chart')]"

    def all_cards(self):
        return self.find_elements_by_xpath(*DashboardPage.dashboard_cards)

    def emp_leave_card_gear_btn(self):
        return self.find_element_by_xpath(*DashboardPage.employee_leave_card_gear_icon)
