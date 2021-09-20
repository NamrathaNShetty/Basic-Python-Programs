'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 01:02  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 01:10
* @Title: To add a key to a dictionary.
'''

from Loggers import logger

def create_tuple():
    """
    Description: 
        This function is to create a tuple.
    """
    try:
        tuple1 = (1, 2, 3, 4, 5)
        logger.info("Tuple created :")
        logger.info(tuple1)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    create_tuple()