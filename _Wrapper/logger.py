import logging
from logging import LoggerAdapter

# Create a logger instance
logger = logging.getLogger(__name__)

# Create a LoggerAdapter instance
logger_adapter = LoggerAdapter(logger, {"extra_key": "extra_value"})

# Now you can use logger_adapter for logging
logger_adapter.log(logging.INFO, "Failure Occurred")
