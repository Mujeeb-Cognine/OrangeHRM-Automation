import requests
from requests.exceptions import RequestException
from APIUtils.APIEndPoints.AdminAPIEndPoints import AdminAPIEndPoints
from BaseUtils.BaseAPIUtils import BaseAPIUtils
from OrangeHRMData.Enums import ApiStatusCodes


class UserAPIs(BaseAPIUtils):

    def create_user(self, username, password, empNumber, status=True, userRoleId=2, max_retries=3):
        """
        :param status:
        :param username:
        :param password:
        :param userRoleId:
        :param empNumber:
        :param max_retries: Number of times to retry the API call in case of failure
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
            "authorization": self.bearer()
        }

        response = None  # Initialize response outside the try block

        for retry_count in range(max_retries):
            try:
                response = requests.post(self.api_url(AdminAPIEndPoints().create_user), json=payload, headers=headers)

                # Print response for debugging
                # print(f"Response: {response.text}")

                # Check if the response status code indicates success
                if response.status_code == ApiStatusCodes().SUCCESS:
                    return
                else:
                    print(f"Failed attempt {retry_count + 1}, Status code: {response.status_code}")
                    response.raise_for_status()  # Raise an exception for non-2xx status codes

            except RequestException as e:
                print(f"Error in attempt {retry_count + 1}: {e}")

        # If the maximum number of retries is reached, raise an exception with the status code
        if response is not None:
            raise Exception(f"Failed to create user after {max_retries} attempts. Last attempt status code: "
                            f"{response.status_code}")
        else:
            raise Exception(f"Failed to create user after {max_retries} attempts. No response received.")
