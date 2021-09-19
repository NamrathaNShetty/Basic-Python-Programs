'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 14:25
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 14:35
* @Title: Program to clone or copy a list.
'''
from Loggers import logger

def clone_list():
    '''
    Description:
        This function clone or copy a list
    '''
    try:

        original_list = [10, 22, 44, 23, 4]
        new_list = list(original_list)
        
        print("Original List is: ",original_list)
        logger.info(original_list)
        print("Cloned List is :", new_list)
        logger.info(new_list)

    except Exception:
        logger.error("invalid Input")

if __name__ == "__main__":
 clone_list()