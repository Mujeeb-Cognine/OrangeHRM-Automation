import logging
import os
import tempfile
from datetime import datetime


class DefaultLog(logging.LoggerAdapter):

    @staticmethod
    def get(level=logging.INFO):
        log_folder_path = os.path.join(tempfile.gettempdir(), 'OrgHRM_Automation_Logs')
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = "OrangeHRM_TestCases_Run"
        log_file_path = os.path.join(log_folder_path, f'{test_name}_{timestamp}.log')

        # Configure logging to write to both console and file
        logging.basicConfig(filename=log_file_path, level=level,
                            format='%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        # Create a logger instance
        logger = logging.getLogger()
        logger.setLevel(level)

        return logger
