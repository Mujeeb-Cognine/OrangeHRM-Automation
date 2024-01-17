import requests

from _Wrapper.BaseClass import BaseClass


class DashBoardApis(BaseClass):

    def config_employees_on_leave_today(self, show_only_accessible_employees_on_leave_today= False):

        payload = {"showOnlyAccessibleEmployeesOnLeaveToday": show_only_accessible_employees_on_leave_today}
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": self.get_bearer_token()
        }

        response = requests.put(f'{self.get_base_url()}/api/v2/admin/users', json=payload, headers=headers)

        print(response.text)
