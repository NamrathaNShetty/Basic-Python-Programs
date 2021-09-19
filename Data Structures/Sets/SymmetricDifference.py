'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 01:02  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 01:08
* @Title: Program to create a symmetric difference.
'''

from Loggers import logger

def symmetric_difference():
    '''
    Description:
        This function to create symmetric difference
    '''
    try:

        set1 = set(["green", "blue"])
        set2 = set(["blue", "yellow"])
        logger.info("Original sets:")
        logger.info(set1)
        logger.info(set2)
        result1 = set1.symmetric_difference(set2)
        logger.info("Symmetric difference of set1 and set2 :")
        logger.info(result1)
        
        set3 = set([1, 1, 2, 3, 4, 5])
        set4 = set([1, 5, 6, 7, 8, 9])
        logger.info("Original sets:")
        logger.info(set3)
        logger.info(set4)
        result2 = set3.symmetric_difference(set4)
        logger.info("Symmetric difference of set3 and set4:")
        logger.info(result2)
        
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    symmetric_difference()    