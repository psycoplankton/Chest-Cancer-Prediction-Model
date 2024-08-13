"""This code sets up logging for a Python application, which is an
essential part of tracking the behavior of the application,
debugging, and recording errors or important events."""

import os
import sys
import logging

"""
logging_str: Defines the format o log messages
    %(asctime)s -> Timestamp of the log entry.
    %(levelname)s -> The log level e.g. INFO, DEBUG, ERROR.
    %(module)s -> The name of the module the generated the log message.
    %(message)s -> The acutal log message.  
"""

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
