'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 16:20
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 16:30
* @Title: Program to find common items from two lists.
'''
from Loggers import logger

def common_items():
    '''
    Description:
        This function finds common items from two lists.
    '''
    try:

        list1 = [1,2,3,4,5,6,7]
        list2 = [2,3,5,7]
        list3 = []

        for item in list1:
            if list2.__contains__(item):
                list3.append(item)

        logger.info("Commom Elements are")
        logger.info(list3)
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
 common_items()