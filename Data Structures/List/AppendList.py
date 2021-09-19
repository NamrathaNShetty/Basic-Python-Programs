'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 15:45
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 16:02
* @Title: Python program to append a list to the second list.
'''
from Loggers import logger

def append():
    """
    Description: Function is used to append one list to another.
    """
    try:
     list1 = [1, 2, 3, 0]
     list2 = ['abc', 'def', 'ghi']
     final_list = list1 + list2
     logger.info(final_list)

    except Exception:
     logger.error("Invalid Input")

if __name__ == "__main__":
 append() 