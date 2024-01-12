from Locators.DashboardPageLocators import DashboardPageLocators
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
