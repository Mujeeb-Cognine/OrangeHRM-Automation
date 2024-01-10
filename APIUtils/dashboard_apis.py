import requests
from conftest import base_url, bearer


class DashBoardApis:

    def config_employees_on_leave_today(self, show_only_accessible_employees_on_leave_today= False):

        payload = {"showOnlyAccessibleEmployeesOnLeaveToday": show_only_accessible_employees_on_leave_today}
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": bearer
        }

        response = requests.put(f'{base_url}/api/v2/admin/users', json=payload, headers=headers)

        print(response.text)
