'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 14:10
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 14:15
* @Title: Program to remove duplicates from a list.
'''
from Loggers import logger

def remove_duplicates():
    '''
    Description:
        This function removes duplicate elements in list
    '''

    try:
        list = [1,2,3,2,1,5,6,4,8,7,5,4]

        dup_items = set()
        
        for x in list:
            if x not in dup_items:
                dup_items.add(x)

        logger.info(dup_items)

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
 remove_duplicates()