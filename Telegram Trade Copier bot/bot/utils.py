import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Set up a logger with a specified name and log file. """
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def log_error(error_messsage):
    """Log an error message."""
    logger = setup_logger("error_logger", "logs/error.log")
    logger.error(error_message)