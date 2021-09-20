'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 09:45  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 09:54
* @Title: Program to remove an item from a tuple.
'''

from Loggers import logger

def remove():
    """
    Description: 
        This function is to remove an item from tuple.
        Tuple is first converted to list, after removing item 
        list is converted back to tuple.
    """
    try:
        
        tuple1 = (1,2,3,4,5,6,7,8)
        logger.info(tuple1)
        
        #tuples are immutable, so you can not remove elements
        #converting the tuple to list
        list1 = list(tuple1) 
        list1.remove(7)
        
        #converting the list to tuple
        tuple2 = tuple(list1) 
        logger.info(tuple2)


    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove()