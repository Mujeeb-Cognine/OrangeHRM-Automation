import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from APIUtils.dashboard_apis import DashBoardApis
from PageFragments.BasePageFragments import BasePageFragments
from PageFragments.DashboardPage import DashboardPage
from BaseUtils.BaseClass import BaseClass


@pytest.mark.usefixtures("admin_login")
class TestDashboard(BaseClass):

    def test_verifying_card_in_dashboard(self, driver: WebDriver):
        dashboard_page = DashboardPage(driver)
        # Verifying the dashboard cards are present in the Dashboard Page.
        self.verify_element_presence(driver, element_locator=dashboard_page.dashboard_cards)

    def test_change_employee_on_leave_today_config(self, driver: WebDriver):

        dashboard_page = DashboardPage(driver)
        # Check if the 'emp_leave_card' is present
        if not self.verify_element_presence(driver, element_locator=dashboard_page.emp_leave_card):
            retry_count = 0
            max_retries = 3

            while retry_count < max_retries:
                # API call
                if DashBoardApis().config_employees_on_leave_today():
                    self.test_change_employee_on_leave_today_config(driver)
                    # If API call is successful, break out of the loop and proceed with the test logic
                    break

                # Increment retry count
                retry_count += 1

                # Added a sleep or delay here to avoid making too many requests in a short time
                time.sleep(2)

            # Check if the API call was successful after maximum retries
            if retry_count == max_retries:
                pytest.fail("API call failed after maximum retries. Test aborted.")
        # Verifying the dashboard cards are present in the Dashboard Page.
        self.verify_element_presence(driver, element_locator=dashboard_page.dashboard_cards)
        base_page_fragments = BasePageFragments(driver)
        self.verify_element_presence(driver, element_locator=dashboard_page.gear_icon)
        # Clicking on employee leave card gear icon.
        dashboard_page.emp_leave_card_gear_btn().click()
        base_page_fragments = BasePageFragments(driver)
        base_page_fragments.wait_until_orng_hrm_dialog_appears()
        # Clicking on toggle button in the dialog.
        base_page_fragments.click_toggle_switch()
        # Clicking on save button in the dialog.
        base_page_fragments.click_orng_hrm_dialog_save()
        # Verifying the success message.
        base_page_fragments.verify_success()

    @pytest.mark.parametrize("admin_login", [{"username": "custom_user", "password": "custom_pass"}], indirect=True)
    def test_change_employee(admin_login, driver: WebDriver):
        dashboard_page = DashboardPage(driver)
        # Verifying the dashboard cards are present in the Dashboard Page.
        admin_login.verify_element_presence(driver, element_locator=dashboard_page.dashboard_cards)
