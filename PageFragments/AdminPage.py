import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _Wrapper.BaseClass import BaseClass
from OrangeHRMData.Constants import Constants
from PageFragments.BasePageFragments import BasePageFragments


@pytest.mark.usefixtures("driver")
class AdminPage(BasePageFragments):

    def __init__(self):
        BaseClass.__init__(self)
        super().__init__()

    def add_user_page(self):
        return AddUser()

    def wait_for_load(self):
        self.wait_for_all_elements_presence(elements_locator="//div[@class='oxd-table-filter']")

    def enter_user_name(self, user_name):
        self.send_keys_to_element(element_locator="//div[@class='oxd-input-group "
                                                  "oxd-input-field-bottom-space']/div/input", keys=user_name)

    def select_user_role(self, user_role):
        self.click_element("(//i[@class='oxd-icon bi-caret-down-fill "
                           "oxd-select-text--arrow'])[1]")
        self.click_element(f"//span[contains(text(), '{user_role}')]")

    def select_employee_name(self, emp_name):
        self.send_keys_to_element("//input[@placeholder='Type for hints...']",
                                  keys=emp_name)
        self.wait_for_element_presence(element_locator=f"//span[contains(text(), '{emp_name}')]")
        self.click_element(f"//span[contains(text(), '{emp_name}')]")

    def select_satus(self, option_name):
        self.click_element("(//i[@class='oxd-icon bi-caret-down-fill "
                           "oxd-select-text--arrow'])[2]")
        self.wait_for_element_presence(element_locator=f"//span[contains(text(), '{option_name}')]")
        self.click_element(f"//span[contains(text(), '{option_name}')]")

    def click_submit_btn(self):
        self.click_element("//button[@type='submit']")

    def search_system_user_by_username(self, username):
        self.enter_user_name(username)
        self.wait_for_element_presence(element_locator="//button[@type='submit']")
        self.click_submit_btn()

    def search_system_user_by_user_role(self, user_role):
        self.select_user_role(user_role)
        self.click_submit_btn()

    def search_system_user_by_emp_name(self, emp_name):
        self.select_employee_name(emp_name)
        self.click_submit_btn()

    def search_system_user_by_status(self, status):
        self.select_satus(status)
        self.click_submit_btn()

    def click_add_button(self):
        self.click_element(element_locator="//button//i[contains(@class,'bi-plus')]")

    def wait_for_add_user_page_load(self):
        self.wait_for_element_presence(element_locator="//div[@class='orangehrm-card-container']")

    def run_add_user_card(self, user_role=None, emp_name=None, status=None, user_name=None, password=None,
                          confirm_password=None, save=None):
        if user_role is not None:
            self.select_user_role(user_role)
        if emp_name is not None:
            self.select_employee_name(emp_name)
        if status is not None:
            self.select_satus(status)
        if user_name is not None:
            self.add_user_page().enter_add_user_user_name(user_name)
        if password is not None:
            self.add_user_page().enter_password(password)
        if confirm_password is not None:
            self.add_user_page().enter_confirm_password(confirm_password)
        if save is not None:
            self.click_save()


class AddUser(AdminPage):

    def enter_add_user_user_name(self, user_name):
        self.send_keys_to_element(element_locator="(//input[@class='oxd-input "
                                                  "oxd-input--active'])[2]", keys=user_name)

    def enter_password(self, password):
        self.send_keys_to_element(element_locator="(//input[@type='password'])[1]",
                                  keys=password)

    def enter_confirm_password(self, confirm_password):
        self.send_keys_to_element(element_locator="(//input[@type='password'])[2]",
                                  keys=confirm_password)
