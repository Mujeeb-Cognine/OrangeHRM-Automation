from OrangeHRMData._BaseLocalizationClass import _BaseNoLocalizationClass


class DashboardPageLocators(_BaseNoLocalizationClass):
    dashboard_cards = "//div[contains(@class,'orangehrm-dashboard-widget-body')]"
    employee_leave_card_gear_icon = "//div[contains(@class,'emp-leave-chart')]//i"
    emp_leave_card = "//div[contains(@class,'emp-leave-chart')]"
