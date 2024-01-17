import time
import pytest
from APIUtils.dashboard_apis import DashBoardApis
from PageFragments.BasePageFragments.BasePageFragments import BasePageFragments
from PageFragments.DashboardPageFragments.DashboardPage import DashboardPage
from _Wrapper.BaseClass import BaseClass


class TestDashboard(BaseClass):

    def test_verifying_card_in_dashboard(self):
        # Verifying the dashboard cards are present in the Dashboard Page.
        DashboardPage().wait_for_load()

    def test_change_employee_on_leave_today_config(self):

        # Check if the 'emp_leave_card' is present
        if not self.wait_for_element_presence(element_locator=DashboardPage().emp_leave_card()):
            retry_count = 0
            max_retries = 3

            while retry_count < max_retries:
                # API call
                if DashBoardApis().config_employees_on_leave_today():
                    self.test_change_employee_on_leave_today_config()
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
        DashboardPage().wait_for_load()
        self.wait_for_element_presence(element_locator=DashboardPage().emp_leave_card_gear_icon())
        # Clicking on employee leave card gear icon.
        self.click_element(element_locator=DashboardPage().emp_leave_card_gear_icon())
        BasePageFragments().wait_until_ornghrm_dialog_appears()
        # Clicking on toggle button in the dialog.
        BasePageFragments().click_toggle_switch()
        # Clicking on save button in the dialog.
        BasePageFragments().click_ornghrm_dialog_save()
        # Verifying the success message.
        BasePageFragments().verify_success()
