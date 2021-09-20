'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 09:35  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 09:41
* @Title: Program to check whether an element exists within a tuple.
'''
from Loggers import logger

def list_to_tuple():
    try:
        list = [1, 2, 3, 4, 5]
        logger.info(list)
        tuple1 = tuple(list)
        logger.info(tuple1)

    except Exception:
      logger.info("Invalid")   

if __name__ == "__main__":
    list_to_tuple()     