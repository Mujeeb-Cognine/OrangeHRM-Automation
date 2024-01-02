import requests
from tests.conftest import bearer, base_url


class AdminApis:

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
            "authorization": bearer
        }

        response = requests.post(f'{base_url}/api/v2/admin/users', json=payload, headers=headers)

        print(response.text)
