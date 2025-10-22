# logger.py
import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
from pathlib import Path


# Create a logger instance
def create_logger():
    # Get the current directory and parent directory for the log path
    current_directory = str(Path(__file__).resolve().parent)
    parent_directory = Path(current_directory).parent


    # Create logger
    logger = logging.getLogger('SEPythExe_logger')
    logger.setLevel(logging.DEBUG)  # Set the root logger level to DEBUG

    # Stream handler with INFO level
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s line %(lineno)d")
    stream_handler.setFormatter(stream_formatter)

    # File handler with DEBUG level and rotating file configuration
    file_handler = RotatingFileHandler(str(parent_directory) + '/logs/SEPythExe.log',
                                       maxBytes=50000,  # 500 KB
                                       backupCount=2)
    file_handler.setLevel(logging.DEBUG) #If level is set higher, for instance at ERROR, then any output for a lower level such as DEBUG will only be print to the terminal and not into a log file
    file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(file_formatter)

    # Add handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


# Instantiate the logger
logger: Logger = create_logger()