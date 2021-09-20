'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 08:50  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 08:55
* @Title: Program to unpack a tuple in several variables.
'''

from Loggers import logger

def unpack_tuple():
    """
    Description: 
        This function to unpack a tuple in several variables
    """
    try:
        tuple1 = (1, 2, 3.4, 'abc')
        
        #unpacking tuple into several variables
        t1, t2, t3, t4 = tuple1

        logger.info(t1)
        logger.info(t2)
        logger.info(t3)
        logger.info(t4)


    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    unpack_tuple()