'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 15:28
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 15:42
* @Title: Python program to print a specified list after removing the 0th, 4th and
5th elements.
'''
from Loggers import logger

def remove_specified():
    '''
    Description:
        to print a list after removing specified elements
    '''
    try:
        list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        list2 = [x for (i,x) in enumerate(list1) if i not in (0,4,5)]
        logger.info(list2)
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
 remove_specified()