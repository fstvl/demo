import os
import logging.config


def get_logger():
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.config.fileConfig(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logger_config.ini'))
    logger = logging.getLogger()
    return logger
