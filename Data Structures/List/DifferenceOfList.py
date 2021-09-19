'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 15:45
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 16:02
* @Title: Python program to get the difference between the two lists.
'''
from Loggers import logger

def difference():
    """
    Description: Function is used to find the difference between two lists.
    """
    try:
     list1 = [1, 3, 5, 7, 9]
     list2=[1, 2, 4, 6, 7, 8]
     diff_list1_list2 = list(set(list1) - set(list2))
     diff_list2_list1 = list(set(list2) - set(list1))
     total_diff = diff_list1_list2 + diff_list2_list1
     logger.info(total_diff)

    except Exception:
     logger.error("Invalid Input")

if __name__ == "__main__":
 difference()   