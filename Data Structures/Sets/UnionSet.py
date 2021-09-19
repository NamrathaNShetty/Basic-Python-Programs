'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 00:36  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 00:40
* @Title: Program to create an union of sets.
'''
from Loggers import logger

def union():
    '''
    Description:
        This function to create union of sets
    '''
    try:
        
        setx = set(["green", "blue"])
        sety = set(["blue", "yellow"])
        logger.info("Original set elements:")
        logger.info(setx)
        logger.info(sety)
        
        logger.info("Union of two sets:")
        setz = setx.union(sety)
        logger.info(setz)
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    union()