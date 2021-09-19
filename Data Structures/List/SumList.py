'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 12:56  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 13:10
* @Title: Program to sum all the items in a list.
'''
from Loggers import logger

def sum_list():
    '''
    Description:
        This function implements sum of all the elements
        in a list.
    '''
    try:
        
        nums = [1, 2, 3, 4, 5]
        print("Sum of the list is :", sum(nums))
        logger.info(sum(nums))

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
 sum_list()