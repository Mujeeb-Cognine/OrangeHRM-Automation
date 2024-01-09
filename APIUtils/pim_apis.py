import requests
from tests.conftest import base_url, bearer


class PIMApis:
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
            "authorization": bearer
        }
        response = requests.post(f'{base_url}/api/v2/pim/employees', json=payload, headers=headers)
        # Print response for debugging
        print(f"Response: {response.text}")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            json_response = response.json()
            emp_number = json_response.get('data', {}).get('empNumber')
            print(f"The employee number is: {emp_number}")
            return emp_number
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
