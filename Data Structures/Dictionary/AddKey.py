'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 12:56  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:10
* @Title: To add a key to a dictionary.
'''

from Loggers import logger

def add_key():
    '''
    Description:
        This function adds the key to dictionary
    '''
    try:
        dict = { 0: 10, 1: 20,}
        logger.info("Before adding the key :")
        logger.info(dict)

        dict.update({2: 30})
        logger.info("After adding the key :")
        logger.info(dict)

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    add_key()