from Locators.AdminPageLocators import AdminUserLocators, AdminAddUserLocators
from _Wrapper.BaseClass import BaseClass
from PageFragments.BasePageFragments.BasePageFragments import BasePageFragments


class AdminPage(BasePageFragments):

    def __init__(self):
        BaseClass.__init__(self)
        super().__init__()

    def add_user_page(self):
        return AddUser()

    def system_user_card(self):
        return AdminUserLocators().system_user_card

    def user_name_field(self):
        return AdminUserLocators().username_field

    def user_role_field_caret_icon(self):
        return AdminUserLocators().user_role_field_caret_icon

    def user_role_option(self):
        return AdminUserLocators().user_role_option

    def emp_name_field(self):
        return AdminUserLocators().emp_name_field

    def emp_name_option(self):
        return AdminUserLocators().emp_name_option

    def status_field_caret_icon(self):
        return AdminUserLocators().status_field_caret_icon

    def status_field_option(self):
        return AdminUserLocators().status_field_option

    def submit_button(self):
        return AdminUserLocators().submit_button

    def add_button(self):
        return AdminUserLocators().add_button

    def aad_user_card(self):
        return AdminUserLocators().add_user_card

    def wait_for_load(self):
        self.wait_for_all_elements_presence(elements_locator=self.system_user_card())

    def enter_user_name(self, user_name):
        self.send_keys_to_element(element_locator=self.user_name_field(), keys=user_name)

    def select_user_role(self, user_role):
        self.click_element(self.user_role_field_caret_icon())
        user_role_option_path = self.user_role_option() % f'"{user_role}"'
        self.click_element(user_role_option_path)

    def select_employee_name(self, emp_name):
        self.send_keys_to_element(self.emp_name_field(), keys=emp_name)
        emp_name_option_path = self.emp_name_option() % f'"{emp_name}"'
        self.wait_for_element_presence(element_locator=emp_name_option_path)
        self.click_element(emp_name_option_path)

    def select_status(self, option_name):
        self.click_element(self.status_field_caret_icon())
        status_field_option_path = self.status_field_option() % f'"{option_name}"'
        self.wait_for_element_presence(element_locator=status_field_option_path)
        self.click_element(status_field_option_path)

    def click_submit_btn(self):
        self.click_element(self.submit_button())

    def search_system_user_by_username(self, username):
        self.enter_user_name(username)
        self.wait_for_element_presence(element_locator=self.submit_button())
        self.click_submit_btn()

    def search_system_user_by_user_role(self, user_role):
        self.select_user_role(user_role)
        self.click_submit_btn()

    def search_system_user_by_emp_name(self, emp_name):
        self.select_employee_name(emp_name)
        self.click_submit_btn()

    def search_system_user_by_status(self, status):
        self.select_status(status)
        self.click_submit_btn()

    def click_add_button(self):
        self.click_element(element_locator=self.add_button())

    def wait_for_add_user_page_load(self):
        self.wait_for_element_presence(element_locator=self.aad_user_card())

    def run_add_user_card(self, user_role=None, emp_name=None, status=None, user_name=None, password=None,
                          confirm_password=None, save=None):
        if user_role is not None:
            self.select_user_role(user_role)
        if emp_name is not None:
            self.select_employee_name(emp_name)
        if status is not None:
            self.select_status(status)
        if user_name is not None:
            self.add_user_page().enter_add_user_user_name(user_name)
        if password is not None:
            self.add_user_page().enter_password(password)
        if confirm_password is not None:
            self.add_user_page().enter_confirm_password(confirm_password)
        if save is not None:
            self.click_save()


class AddUser(AdminPage):

    def user_name_field(self):
        return AdminAddUserLocators().user_name_field

    def password_field(self):
        return AdminAddUserLocators().password_field

    def confirm_password_field(self):
        return AdminAddUserLocators().confirm_password_field

    def enter_add_user_user_name(self, user_name):
        self.send_keys_to_element(element_locator=self.user_name_field(), keys=user_name)

    def enter_password(self, password):
        self.send_keys_to_element(element_locator=self.password_field(), keys=password)

    def enter_confirm_password(self, confirm_password):
        self.send_keys_to_element(element_locator=self.confirm_password_field(), keys=confirm_password)
