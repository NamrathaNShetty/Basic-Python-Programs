'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 09:25  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 09:34
* @Title: Program to check whether an element exists within a tuple.
'''

from Loggers import logger

def check_element():
    try:
    
     tuple1 = ('a', 'b', 'c', 'd', 5, 4, 7)
     logger.info("r" in tuple1)
     logger.info(5 in tuple1)

    except Exception:
     logger.error("Invalid")

if __name__ == "__main__":
    check_element()     