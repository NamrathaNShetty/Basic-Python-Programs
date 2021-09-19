'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 17:20
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 17:30
* @Title: Program to split a list based on first character of word.
'''

from Loggers import logger
import itertools

def remove():
    '''
    Description:
        Removes duplicates from list of list
    '''

    try:
        
        num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        logger.info("Original list")
        logger.info(num)
        
        num.sort()
        
        new_num = list(num for num,_ in itertools.groupby(num))
        logger.info("New list")
        logger.info(new_num)

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
 remove()
