from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DriverWidgets.DriverInitialization import DriverInitialization
from OrangeHRMData.Constants import Constants


class BasePageFragments(DriverInitialization):

    def __init__(self):
        DriverInitialization.__init__(self)

    def verify_element_presence(self, element_locator):
        try:
            WebDriverWait(self.driver, timeout=Constants.short_live_throttle).until(
                EC.presence_of_element_located(element_locator))
            return True
        except TimeoutException:
            return False

    def navigate_to_menu(self, menu_name):
        menu_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'oxd-main-menu-button')]")
        if "bi-chevron-left" not in menu_button.get_attribute("class"):
            self.driver.find_element(By.XPATH, f"//span[normalize-space()='{menu_name}']").click()
        else:
            menu_button.click()
            WebDriverWait(self.driver, timeout=Constants.short_live_throttle).until(
                EC.presence_of_all_elements_located((By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']")))
            self.driver.find_element(By.XPATH, f"//span[normalize-space()='{menu_name}']").click()

    def search_and_select_menu(self, menu_name):
        menu_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'oxd-main-menu-button')]")
        if "bi-chevron-left" not in menu_button.get_attribute("class"):
            self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(menu_name)
            self.driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']").click()
        else:
            menu_button.click()
            WebDriverWait(self.driver, timeout=Constants.short_live_throttle).until(
                EC.presence_of_element_located((By.XPATH, "//ul[@class='oxd-main-menu']")))
            self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(menu_name)
            self.driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']").click()

    def click_grid_checkbox_after_filter(self):
        self.driver.find_element(By.XPATH,
                                 "//div[@class='oxd-table-card-cell-checkbox']//input[@type='checkbox']").click()

    def click_delete_icon(self):
        self.driver.find_element(By.XPATH, "//i[contains(@class,'bi-trash')]").click()

    def click_checkbox(self):
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

    def click_yes_or_delete_in_dialog(self):
        self.driver.find_element(
            By.XPATH, "//div[contains(@class,'orangehrm-dialog-popup')]//button[@type='button'][2]").click()

    def click_no_or_cancel_in_dialog(self):
        self.driver.find_element(
            By.XPATH, "//div[contains(@class,'orangehrm-dialog-popup')]//button[@type='button'][1]").click()

    def wait_until_grid_loads(self):
        WebDriverWait(self.driver, timeout=Constants.short_live_throttle).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class ='oxd-table-body']")))

    def wait_until_confirmation_dialog_appears(self):
        WebDriverWait(self.driver, timeout=Constants.short_live_throttle).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'orangehrm-dialog-popup')]")))

    def verify_success(self):
        WebDriverWait(self.driver, timeout=Constants.short_live_throttle).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[contains(@class,'oxd-toast-container')]//p[text()='Success']")))
        (self.driver.find_element(By.XPATH, "//div[contains(@class,'oxd-toast-container')]//p[text()='Success']")
         .is_displayed())

    def wait_until_orng_hrm_dialog_appears(self):
        WebDriverWait(self.driver, timeout=Constants.short_live_throttle).until(
            EC.presence_of_element_located((
                By.XPATH, "//div[contains(@class,'orangehrm-dialog-modal')]//button[@type='button']")))

    def click_orng_hrm_dialog_save(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def click_toggle_switch(self):
        WebDriverWait(self.driver, timeout=Constants.default_throttle).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'oxd-switch-input')]")))
        self.driver.find_element(By.XPATH, "//span[contains(@class,'oxd-switch-input')]").click()

    def click_cancel(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def click_save(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
