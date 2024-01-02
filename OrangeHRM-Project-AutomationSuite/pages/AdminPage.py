from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DefaultData.OrangeHRMData import TimeoutConstants
from pages.BasePageFargments import BasePageFragments


class AdminPage(BasePageFragments):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def add_user_page(self):
        return AddUser(self.driver)

    def wait_for_load(self):
        WebDriverWait(self.driver, timeout=TimeoutConstants.default).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-filter']")))

    def enter_user_name(self, user_name):
        self.driver.find_element(By.XPATH, "//div[@class='oxd-input-group "
                                           "oxd-input-field-bottom-space']/div/input").send_keys(user_name)

    def select_user_role(self, user_role):
        self.driver.find_element(By.XPATH,
                                 "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{user_role}')]").click()

    def select_employee_name(self, emp_name):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(emp_name)
        WebDriverWait(self.driver, timeout=TimeoutConstants.default).until(
            EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{emp_name}')]")))
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{emp_name}')]").click()

    def select_satus(self, option_name):
        self.driver.find_element(By.XPATH,
                                 "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]").click()
        WebDriverWait(self.driver, timeout=TimeoutConstants.default).until(
            EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{option_name}')]")))
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{option_name}')]").click()

    def click_submit_btn(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def search_system_user_by_username(self, username):
        self.enter_user_name(username)
        WebDriverWait(self.driver, timeout=TimeoutConstants.default).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
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
        self.driver.find_element(By.XPATH, "//button//i[contains(@class,'bi-plus')]").click()

    def wait_for_add_user_page_load(self):
        WebDriverWait(self.driver, timeout=TimeoutConstants.default).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='orangehrm-card-container']")))

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

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def enter_add_user_user_name(self, user_name):
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(user_name)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys(confirm_password)
