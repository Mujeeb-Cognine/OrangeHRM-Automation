from Locators.LoginPageLocators import LoginPageLocators
from OrangeHRMData.Constants import Constants
from PageFragments.BasePageFragments.BasePageFragments import BasePageFragments
from _Wrapper.BaseClass import BaseClass


class LoginPage(BasePageFragments):

    def __init__(self):
        BaseClass.__init__(self)

    def username_field(self):
        return LoginPageLocators().user_name_field

    def password_field(self):
        return LoginPageLocators().password_field

    def submit_btn(self):
        return LoginPageLocators().submit_button

    def wait_for_load(self, timeout=Constants.default_throttle):
        self.verify(lambda: self.verify_elements_present(self.username_field()), timeout=timeout,
                    fail_message="No username field exists")

    def enter_username_field(self, username):
        self.send_keys_to_element(element_locator=self.username_field(), keys=username)

    def enter_password_field(self, password):
        self.send_keys_to_element(element_locator=self.password_field(), keys=password)

    def click_submit_btn(self):
        self.click_element(element_locator=self.submit_btn())

    def run_login(self, username=None, password=None, submit_btn=True, timeout=Constants.default_throttle):
        self.wait_for_load(timeout)
        if username is not None:
            self.enter_username_field(username)
        if password is not None:
            self.enter_password_field(password)
        if submit_btn is True:
            self.click_submit_btn()
