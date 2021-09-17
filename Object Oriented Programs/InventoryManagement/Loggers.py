import logging

logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='inventory.log', level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='inventory.log', level=logging.WARNING,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')