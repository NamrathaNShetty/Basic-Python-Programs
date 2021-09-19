'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 23:04  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 23:15
* @Title: Program to add member(s) in a set.
'''

from Loggers import logger

def add_member():
    '''
    Description:
        This function to Add members to a set
    '''
    try:

        # New empty set
        set1 = set()
        logger.info(set1)
        
        # Adding a single element using add
        logger.info("Add single element:")
        set1.add("Red")
        logger.info(set1)
        
        # Adding multiple elements using update
        logger.info("Add multiple items:")
        set1.update(["Blue", "Green"])
        logger.info(set1)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    add_member()