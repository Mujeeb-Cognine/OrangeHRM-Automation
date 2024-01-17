import requests

from OrangeHRMData.Enums import ApiStatusCodes
from _Wrapper.BaseClass import BaseClass


class PIMApis(BaseClass):
    def create_employee(self, last_name, first_name, employee_id, middle_name=''):
        payload = {
            "lastName": last_name,
            "firstName": first_name,
            "middleName": middle_name,
            "employeeId": employee_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": self.get_bearer_token()
        }
        response = requests.post(f'{self.get_base_url()}/api/v2/pim/employees', json=payload, headers=headers)
        # Print response for debugging
        print(f"Response: {response.text}")

        # Check if the request was successful (status code 200)
        if response.status_code == ApiStatusCodes.SUCCESS:
            json_response = response.json()
            emp_number = json_response.get('data', {}).get('empNumber')
            print(f"The employee number is: {emp_number}")
            return emp_number
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
