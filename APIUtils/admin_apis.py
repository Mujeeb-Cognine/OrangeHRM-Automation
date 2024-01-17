import requests

from _Wrapper.BaseClass import BaseClass


class AdminApis(BaseClass):

    def create_user(self, username, password, empNumber, status=True, userRoleId=2):
        """
        :param status:
        :param username:
        :param password:
        :param userRoleId:
        :param empNumber:
        :return:
        """
        payload = {
            "status": status,
            "username": username,
            "password": password,
            "userRoleId": userRoleId,  # For Admin role = 1 and for ESS role = 2
            "empNumber": empNumber
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": self.get_bearer_token()
        }

        response = requests.post(f'{self.get_base_url()}/api/v2/admin/users', json=payload, headers=headers)

        print(response.text)
