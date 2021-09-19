'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 13:11  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 13:15
* @Title: Program to multiplies all the items in a list.
'''

from Loggers import logger

def multiply_list():
    '''
    Description:
        This function implements multiply all the elements
        in a list.
    '''
    try:
        # Multiplying elements one by one
        items = [1, 2, 3, 4, 5]
        multiply = 1
        for x in items:
            multiply = multiply * x
        
        logger.info(multiply)

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
 multiply_list()