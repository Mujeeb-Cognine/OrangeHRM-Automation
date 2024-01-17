from Locators.DashboardPageLocators import DashboardPageLocators
from OrangeHRMData.Constants import Constants
from _Wrapper.BaseClass import BaseClass
from PageFragments.BasePageFragments.BasePageFragments import BasePageFragments


class DashboardPage(BasePageFragments):

    def __init__(self):
        BaseClass.__init__(self)

    def dashboard_cards(self):
        return DashboardPageLocators().dashboard_cards

    def emp_leave_card_gear_icon(self):
        return DashboardPageLocators().employee_leave_card_gear_icon

    def emp_leave_card(self):
        return DashboardPageLocators().emp_leave_card

    def wait_for_load(self, timeout=Constants.default_throttle):
        self.verify(lambda: self.verify_element_present(self.dashboard_cards()), timeout=timeout,
                    fail_message="No dashboard cards are present")
