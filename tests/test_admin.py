import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from DefaultData.OrangeHRMData import MenuItems, AdminUserRoles, AdminStatus
from APIUtils.admin_apis import AdminApis
from APIUtils.pim_apis import PIMApis
from PageFragments.AdminPage import AdminPage
from PageFragments.BasePageFragments import BasePageFragments
from BaseUtils.BaseClass import BaseClass
from BaseUtils.Dataset import Dataset


@pytest.mark.usefixtures("admin_login")
class TestAdmin(BaseClass):

    def test_add_user(self, driver: WebDriver):
        # Creating the test data.
        test_data = Dataset()
        # Creating an employee.
        PIMApis().create_employee(last_name=test_data.last_name, first_name=test_data.first_name,
                                  middle_name=test_data.middle_name, employee_id=test_data.emp_id)
        base_page_fragments = BasePageFragments(driver)
        # Navigating to the Admin Side menu.
        base_page_fragments.navigate_to_menu(menu_name=MenuItems.admin)

        admin_page = AdminPage(driver)
        admin_page.wait_for_load()
        # Navigating to Add User page
        admin_page.click_add_button()
        admin_page.wait_for_add_user_page_load()
        # Filling the form and saving the user.
        admin_page.run_add_user_card(user_role=AdminUserRoles.admin, emp_name=test_data.full_name,
                                     status=AdminStatus.enabled, user_name=test_data.user_name,
                                     password=test_data.password, confirm_password=test_data.password, save=True)
        # Verifying the Success.
        base_page_fragments.verify_success()

    def test_user_delete(self, driver: WebDriver):
        # Creating the test data.
        test_data = Dataset()
        # Creating an employee.
        emp_num = PIMApis().create_employee(last_name=test_data.last_name, first_name=test_data.first_name,
                                            employee_id=test_data.emp_id)
        # Creating a user with the created employee.
        AdminApis().create_user(username=test_data.user_name, password=test_data.password, empNumber=emp_num)

        base_page_fragments = BasePageFragments(driver)
        # Navigating to the Admin Side menu.
        base_page_fragments.navigate_to_menu(menu_name=MenuItems.admin)

        admin_page = AdminPage(driver)
        admin_page.wait_for_load()
        # Searching for the created User.
        admin_page.search_system_user_by_username(test_data.user_name)
        base_page_fragments.wait_until_grid_loads()

        # Deleting the User.
        base_page_fragments.click_delete_icon()
        base_page_fragments.wait_until_confirmation_dialog_appears()
        base_page_fragments.click_yes_or_delete_in_dialog()
        # Verifying the Success.
        base_page_fragments.verify_success()
