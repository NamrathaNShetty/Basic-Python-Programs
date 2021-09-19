'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 00:28  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 00:35
* @Title: Program to create an intersection of sets.
'''
from Loggers import logger

def intersection():
    '''
    Description:
        This function to create intersection of sets
    '''
    try:
        
        setx = set(["green", "blue"])
        sety = set(["blue", "yellow"])
        logger.info("Original set elements:")
        logger.info(setx)
        logger.info(sety)
        
        logger.info("Intersection of two sets:")
        setz = setx.intersection(sety)
        logger.info(setz)
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    intersection()