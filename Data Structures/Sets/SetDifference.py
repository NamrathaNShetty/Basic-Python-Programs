'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 00:41  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 00:52
* @Title: Program to create set difference.
'''
from Loggers import logger

def difference():
    '''
    Description:
        This function to create set difference
    '''
    try:

        set1 = set(["green", "blue"])
        set2 = set(["blue", "yellow"])
        logger.info("Original sets:")
        logger.info(set1)
        logger.info(set2)
        result1 = set1.difference(set2)
        logger.info("Difference of set1 - set2:")
        logger.info(result1)
        result2 = set2.difference(set1)
        logger.info("Difference of set2 - set1:")
        logger.info(result2)
        
        set3 = set([1, 1, 2, 3, 4, 5])
        set4 = set([1, 5, 6, 7, 8, 9])
        logger.info("Original sets:")
        logger.info(set3)
        logger.info(set4)
        result3 = set3.difference(set4)
        logger.info("Difference of set3 - set4:")
        logger.info(result3)
        result4 = set4.difference(set3)
        logger.info("Difference of set4 - setn:")
        logger.info(result4)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    difference()    