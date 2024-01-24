import os
import tempfile
from datetime import datetime


class Paths:

    def screenshot_path(self, test_name):
        # Create the base folder if it doesn't exist
        base_folder = os.path.join(tempfile.gettempdir(), 'OrgHRM_Automation_Tests_Screenshot')
        os.makedirs(base_folder, exist_ok=True)

        # Create a sub-folder for each test case
        test_folder = os.path.join(base_folder, test_name)
        os.makedirs(test_folder, exist_ok=True)

        # Generate a timestamp for the screenshot filename
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        return os.path.join(test_folder, f"{test_name}_{timestamp}_failure.png")

    def loggers_path(self):
        log_folder_path = os.path.join(tempfile.gettempdir(), 'OrgHRM_Automation_Logs')
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = "OrangeHRM_TestCases_Run"
        return os.path.join(log_folder_path, f'{test_name}_{timestamp}.log')
