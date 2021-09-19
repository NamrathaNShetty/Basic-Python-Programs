'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 22:32  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 22:45
* @Title: Program to create a set.
'''

from logging import log
from Loggers import logger

def create_set():
    '''
    Description:
        This function creates a set.
    '''
    try:
        
        # Empty set
        logger.info("Create a new set:")
        x = set()
        logger.info(x)

        # Non empty set
        logger.info("Create a non empty set:")
        n = set([0, 1, 2, 3, 4])
        logger.info(n)
    
        # Having mixed type of values
        logger.info("Using a literal:")
        a = {1,2,3,'foo','bar'}
        logger.info(a)
        
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    create_set()