'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 09:15  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 09:22
* @Title: Program to find the repeated items of a tuple.
'''

from Loggers import logger

def count():
    """
    Description: 
        This function is to  create a tuple and count the repeated element.
    """
    
    try:

    #create a tuple
     tuple1 = (2, 4, 5, 6, 2, 3, 4, 4, 7)
     logger.info(tuple1)
     find = int(input("Enter number to find its count: "))
     #return the number of times it appears in the tuple.
     count = tuple1.count(find)
     logger.info(count)

    except Exception:
     logger.error("Invalid")

if __name__ == "__main__":
    count()