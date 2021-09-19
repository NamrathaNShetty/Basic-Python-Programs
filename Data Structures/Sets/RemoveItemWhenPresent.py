'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 00:15  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 00:25
* @Title: Program to remove an item from a set if it is present in the set.
'''
from Loggers import logger

def remove_item():
    '''
    Description:
        This function to remove items, if it is present in a set
    '''
    
    try:
        
        #Create a new set
        set1 = set([0, 1, 2, 3, 4, 5])
        logger.info("Original set elements:")
        logger.info(set1)
        
        logger.info("Remove 0 from the set:")
        set1.discard(4)
        logger.info(set1)
        
        logger.info("Remove 5 from the said set:")
        set1.discard(5)
        logger.info(set1)
        
        logger.info("Remove 2 from the said set:")
        set1.discard(5)
        logger.info(set1)
        
        logger.info("Remove 7 from the said set:")
        set1.discard(15)
        logger.info(set1)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove_item()