import logging

logger = logging
   
# logging basic config method with info and error level.
logger.basicConfig(filename='list.log', level=logging.INFO,
format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='list.log', level=logging.ERROR,
format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')