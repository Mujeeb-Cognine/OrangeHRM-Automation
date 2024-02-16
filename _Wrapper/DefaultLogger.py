import logging

from _Wrapper.Paths import Paths


class DefaultLog(logging.LoggerAdapter):

    @staticmethod
    def get(logger_name, level=logging.INFO):
        log_file_path = Paths().loggers_path()

        # Configure logging to write to file
        logging.basicConfig(filename=log_file_path, level=level,
                            format='%(asctime)s [%(levelname)s] %(funcName)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        # Create a logger instance with the provided name
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

        return DefaultLog(logger, {})
