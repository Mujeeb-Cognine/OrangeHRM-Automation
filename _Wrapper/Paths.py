import os
import tempfile
from datetime import datetime


class Paths:

    def report_and_screenshot_path(self, test_name):
        # Create the base folder if it doesn't exist
        user_profile = os.path.expandvars('%USERPROFILE%')
        temp_dir = os.path.join(user_profile, 'AppData', 'Local', 'Temp')
        base_folder = os.path.join(user_profile, temp_dir, 'OrgHRM_Automation_Tests_Screenshot')
        os.makedirs(base_folder, exist_ok=True)

        file_name = os.path.basename(test_name)
        full_path = os.path.join(base_folder, file_name)
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        # Create a simple PNG file (This can be replaced this with your actual image creation logic)
        with open(full_path, 'wb') as f:
            # Write a minimal PNG header
            f.write(b'\x89PNG\r\n\x1a\n')
            # Write an empty IHDR chunk (13 bytes)
            f.write(b'\x00\x00\x00\rIHDR\x00\x00\x00d\x00\x00\x00d\x08\x06\x00\x00\x00\x1f\x15\xc4\x89')
            # Write an empty IDAT chunk (12 bytes)
            f.write(b'\x00\x00\x00\x0cIDAT\x00\x00\x00\x00IEND\xaeB`\x82')

        return full_path

    def loggers_path(self):
        log_folder_path = os.path.join(tempfile.gettempdir(), 'OrgHRM_Automation_Logs')
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = "OrangeHRM_TestCases_Run"
        return os.path.join(log_folder_path, f'{test_name}_{timestamp}.log')
