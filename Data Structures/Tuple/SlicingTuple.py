'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 09:45  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 09:54
* @Title: Program to slice a tuple.
'''
from Loggers import logger

def slicing():

 try:

    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)

    logger.info(tuple1[1:]) # slicing starts from 1 to end

    logger.info(tuple1[:5]) # slicing starts from 0 and ends at 5th index
    
    logger.info(tuple1[1:4]) # slicing from 1 to 4 

    logger.info(tuple1[::2]) # slicing from start to end using step sizes of 2

 except Exception:
    logger.error("Invalid input")

if __name__ == "__main__":
   slicing()  