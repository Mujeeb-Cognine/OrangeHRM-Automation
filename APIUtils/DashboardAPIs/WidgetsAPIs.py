import requests
from requests.exceptions import RequestException
from APIUtils.APIEndPoints.DashboardAPIEndPoints import DashboardAPIEndPoints
from BaseUtils.BaseAPIUtils import BaseAPIUtils
from OrangeHRMData.Enums import ApiStatusCodes


class WidgetsAPIs(BaseAPIUtils):

    def config_employees_on_leave_today(self, show_only_accessible_employees_on_leave_today=False, max_retries=3):
        """
        :param show_only_accessible_employees_on_leave_today:
        :param max_retries: Number of times to retry the API call in case of failure
        :return:
        """
        payload = {"showOnlyAccessibleEmployeesOnLeaveToday": show_only_accessible_employees_on_leave_today}
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": self.bearer()
        }

        response = None  # Initialize response outside the try block

        for retry_count in range(max_retries):
            try:
                response = requests.put(self.api_url(DashboardAPIEndPoints().config_emp_on_leave_today), json=payload,
                                        headers=headers)

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

            # Add a delay or other handling if needed

        # If the maximum number of retries is reached, print a message with status code
        if response is not None:
            print(f"Failed to configure employees on leave today after {max_retries} attempts. Last attempt status "
                  f"code: {response.status_code}")
        else:
            print(f"Failed to configure employees on leave today after {max_retries} attempts. No response received.")
