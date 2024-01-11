import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _Wrapper.BaseClass import BaseClass
from OrangeHRMData.Constants import Constants


class BasePageFragments(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

    def navigate_to_menu(self, menu_name):
        menu_button = self.find_element_by_xpath("//button[contains(@class, 'oxd-main-menu-button')]")
        if "bi-chevron-left" not in menu_button.get_attribute('class'):
            self.find_element_by_xpath(f"//span[normalize-space()='{menu_name}']").click()
        else:
            self.click_element(menu_button)
            self.wait_for_all_elements_presence(
                elements_locator="//li[@class='oxd-main-menu-item-wrapper']")
            self.find_element_by_xpath(f"//span[normalize-space()='{menu_name}']").click()

    def search_and_select_menu(self, menu_name):
        menu_button = self.find_element_by_xpath("//button[contains(@class, 'oxd-main-menu-button')]")
        if "bi-chevron-left" not in self.get_attribute(element_locator=menu_button, attribute_name="class"):
            self.send_keys_to_element(element_locator="//input[@placeholder='Search']", keys=menu_name)
            self.click_element(element_locator="//ul[@class='oxd-main-menu']")
        else:
            self.click_element(menu_button)
            self.wait_for_element_presence(element_locator="//ul[@class='oxd-main-menu']")
            self.send_keys_to_element(element_locator="//input[@placeholder='Search']", keys=menu_name)
            self.click_element(element_locator="//ul[@class='oxd-main-menu']")

    def click_grid_checkbox_after_filter(self):
        self.click_element(element_locator="//div[@class='oxd-table-card-cell-checkbox']//input["
                                           "@type='checkbox']")

    def click_delete_icon(self):
        self.click_element(element_locator="//i[contains(@class,'bi-trash')]")

    def click_checkbox(self):
        self.click_element(element_locator="//input[@type='checkbox']")

    def click_yes_or_delete_in_dialog(self):
        self.click_element(element_locator="//div[contains(@class,"
                                           "'orangehrm-dialog-popup')]//button["
                                           "@type='button'][2]")

    def click_no_or_cancel_in_dialog(self):
        self.click_element(element_locator="//div[contains(@class,"
                                           "'orangehrm-dialog-popup')]//button["
                                           "@type='button'][1]")

    def wait_until_grid_loads(self):
        self.wait_for_element_presence(element_locator="//div[@class ='oxd-table-body']")

    def wait_until_confirmation_dialog_appears(self):
        self.wait_for_element_presence(element_locator="//div[contains(@class,'orangehrm-dialog-popup')]")

    def verify_success(self):
        self.wait_for_element_presence(element_locator=
                                       "//div[contains(@class,'oxd-toast-container')]//p[text("
                                       ")='Success']")
        self.is_element_displayed("//div[contains(@class,'oxd-toast-container')]//p[text("
                                  ")='Success']")

    def wait_until_orng_hrm_dialog_appears(self):
        self.wait_for_element_presence(element_locator="//div[contains(@class,"
                                                       "'orangehrm-dialog-modal')]//button[@type='button']")

    def click_orng_hrm_dialog_save(self):
        self.click_element("//button[@type='submit']")

    def click_toggle_switch(self):
        self.wait_for_element_presence(element_locator="//div[contains(@class,"
                                                       "'oxd-switch-wrapper')]//label//span",
                                       timeout=Constants.default_throttle)
        time.sleep(2)  # Added sleep as it is taking time to render on the UI.
        self.click_element("//span[contains(@class,'oxd-switch-input')]")

    def click_cancel(self):
        self.click_element("//button[normalize-space()='Cancel']")

    def click_save(self):
        self.click_element("//button[normalize-space()='Save']")
