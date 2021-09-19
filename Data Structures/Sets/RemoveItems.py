'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 23:15  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 23:25
* @Title: Program to remove member(s) in a set.
'''

from Loggers import logger

def remove_item():
    '''
    Description:
        This function to remove items from a set
    '''

    try:
        set1 = set([0, 1, 2, 3, 4, 5])
        logger.info("Original set:")
        logger.info(set1)
        
        # Pop method to remove an element
        set1.pop()
        logger.info("After removing the first element from the said set:")
        logger.info(set1)

        # Remove method to remove an element
        set1.remove(5)
        logger.info("After removing 5 from the set:")
        logger.info(set1)


    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove_item()