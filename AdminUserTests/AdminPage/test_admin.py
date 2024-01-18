from APIUtils.AdminAPIs.UserAPIs import UserAPIs
from APIUtils.PIMAPIs.EmployeeAPIs import EmployeeApis
from PageFragments.AdminPageFragments.AdminPage import AdminPage
from PageFragments.BasePageFragments.BasePageFragments import BasePageFragments
from _Wrapper.BaseClass import BaseClass
from BaseUtils.Dataset import Dataset


#
class TestAdmin(BaseClass):

    def test_add_user(self):
        # Creating the test data.
        test_data = Dataset()
        # Creating an employee.
        EmployeeApis().create_employee(last_name=test_data.last_name, first_name=test_data.first_name,
                                       middle_name=test_data.middle_name, employee_id=test_data.emp_id)
        # Navigating to the Admin Side menu.
        BasePageFragments().navigate_to_menu(menu_name=self.s.menu.admin)

        AdminPage().wait_for_load()
        # Navigating to Add User page
        AdminPage().click_add_button()
        AdminPage().wait_for_add_user_page_load()
        # Filling the form and saving the user.
        AdminPage().run_add_user_card(user_role=self.s.dd.admin_user_roles.admin, emp_name=test_data.full_name,
                                      status=self.s.dd.admin_status.enabled, user_name=test_data.user_name,
                                      password=test_data.password, confirm_password=test_data.password, save=True)
        # Verifying the Success.
        BasePageFragments().verify_success()

    # Override the admin_login fixture for this test method
    def test_user_delete(self):
        # Creating the test data.
        test_data = Dataset()
        # Creating an employee.

        emp_num = EmployeeApis().create_employee(last_name=test_data.last_name, first_name=test_data.first_name,
                                                 employee_id=test_data.emp_id)
        # Creating a user with the created employee.
        UserAPIs().create_user(username=test_data.user_name, password=test_data.password, empNumber=emp_num)

        # Navigating to the Admin Side menu.
        BasePageFragments().navigate_to_menu(menu_name=self.s.menu.admin)

        AdminPage().wait_for_load()
        # Searching for the created User.
        AdminPage().search_system_user_by_username(test_data.user_name)
        BasePageFragments().wait_until_grid_loads()

        # Deleting the User.
        BasePageFragments().click_delete_icon()
        BasePageFragments().wait_until_confirmation_dialog_appears()
        BasePageFragments().click_yes_or_delete_in_dialog()
        # Verifying the Success.
        BasePageFragments().verify_success()
