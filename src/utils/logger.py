# utils/logger.py

import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """
    Function to set up as many loggers as you want
    """

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

# Initialize global logger
if not os.path.exists('logs'):
    os.makedirs('logs')

log_file = os.path.join('logs', 'application.log')
logger = setup_logger('global_logger', log_file)

