'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 01:35 
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 01:58
* @Title: Program to find maximum and the minimum value in a set.
'''

from Loggers import logger

def max_min():
    '''
    Description:
        This function finds maximum and minimum value in a set
    '''
    try:

        # Create a set
        set1 = {5, 10, 3, 15, 2, 20}
        logger.info("Original set elements:")
        logger.info(set1)
        
        # Find the maximum
        logger.info("Maximum value of the set:")
        logger.info(max(set1))
         
        # Find the minimum
        logger.info("Minimum value of the set:")
        logger.info(min(set1))

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    max_min()