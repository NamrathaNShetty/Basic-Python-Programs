'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 01:10 
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 01:15
* @Title: Program to clear te set.
'''
from Loggers import logger

def clear_set():
    '''
    Description:
        This function clears a set
    '''
    try:
        set1 = {"Red", "Green", "Black", "White"}
        logger.info("Original set elements:")
        logger.info(set1)        
        logger.info("After removing all elements of the set :")
        set1.clear()
        logger.info(set1)
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    clear_set()   