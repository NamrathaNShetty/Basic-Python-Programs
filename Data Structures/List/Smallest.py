'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 13:16  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 13:20
* @Title: Program to get the smallest number from a list.
'''

from Loggers import logger

def smallest_list():
    """
    Description: 
        This function is to get smallest number in a list.
    """
    try:
        
        nums = [1, 2, 3, 4, 5]
        print("Smallest of the list is :", min(nums))
        logger.info(min(nums))

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
 smallest_list()