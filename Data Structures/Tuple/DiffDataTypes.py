'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 01:11  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 01:15
* @Title: Program to create a tuple with different data types.
'''

from Loggers import logger

def diff_datatype():
    """
    Description: 
        This function is to create a tuple with different data types
    """
    try:
        tuple1 = (1, 2, 3, 4, 5,'abc',1.2)
        logger.info("Tuple created :")
        logger.info(tuple1)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    diff_datatype()