import os
import logging
from logging.handlers import RotatingFileHandler

from logging.config import fileConfig
import project.utils.color

prefix_path = os.path.dirname(os.path.abspath(__file__))
final_path = os.path.join(prefix_path, 'logging_config.ini')
fileConfig(final_path)

logger = logging.getLogger()

logger.debug("Logger configuration path [%s]", final_path)

if __name__ == '__main__':
    logger.debug("heklad")
    logger.info('asdasda')
