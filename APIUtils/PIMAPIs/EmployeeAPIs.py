import requests
from requests.exceptions import RequestException
from APIUtils.APIEndPoints.PIMAPIEndPoints import PIMAPIEndPoints
from BaseUtils.BaseAPIUtils import BaseAPIUtils
from OrangeHRMData.Enums import ApiStatusCodes


class EmployeeApis(BaseAPIUtils):
    def create_employee(self, last_name, first_name, employee_id, middle_name='', max_retries=3):
        """
        :param last_name:
        :param first_name:
        :param employee_id:
        :param middle_name:
        :param max_retries: Number of times to retry the API call in case of failure
        :return: Employee number if the request is successful, None otherwise
        """
        payload = {
            "lastName": last_name,
            "firstName": first_name,
            "middleName": middle_name,
            "employeeId": employee_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": self.bearer()
        }

        response = None  # Initialize response outside the try block

        for retry_count in range(max_retries):
            try:
                response = requests.post(self.api_url(PIMAPIEndPoints().create_emp), json=payload, headers=headers)

                # Print response for debugging
                # print(f"Response: {response.text}")

                # Check if the request was successful (status code 200)
                if response.status_code == ApiStatusCodes().SUCCESS:
                    json_response = response.json()
                    emp_number = json_response.get('data', {}).get('empNumber')
                    return emp_number
                else:
                    print(f"Failed attempt {retry_count + 1}, Status code: {response.status_code}")
                    response.raise_for_status()  # Raise an exception for non-2xx status codes

            except RequestException as e:
                print(f"Error in attempt {retry_count + 1}: {e}")

        # If the maximum number of retries is reached, print a message with status code and return None
        if response is not None:
            print(f"Failed to create employee after {max_retries} attempts. Last attempt status code: "
                  f"{response.status_code}")
        else:
            print(f"Failed to create employee after {max_retries} attempts. No response received.")
        return None
