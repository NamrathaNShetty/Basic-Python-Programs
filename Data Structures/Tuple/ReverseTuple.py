'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 09:45  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 09:54
* @Title: Program to reverse a tuple.
'''

from Loggers import logger

def reverse():
 """
 Description: 
        This function is to reverse a tuple.
 """
 try:

    tuple1 = ("Reverse")

    tuple2 = reversed(tuple1)

    logger.info(tuple(tuple2))

    tupl1 = (5, 10, 15, 20)

    tupl2 = reversed(tupl1)

    logger.info(tuple(tupl2))

 except Exception:
    logger.error("Invalid Input")

if __name__ == "__main__":
    reverse()    