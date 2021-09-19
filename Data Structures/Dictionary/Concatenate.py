'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 13:20  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:37
* @Title: To concatenate  dictionaries to create a new
'''

from Loggers import logger

def concatenate():
    '''
    Description: 
        This function concatenates dictionaries to 
        create a new one
    '''

    try:

        dict1 = { 0: 10, 1: 20}
        dict2 = { 2: 30, 3: 40}
        dict3 = { 4: 50, 5: 60}
        dict = {}

        for d in (dict1, dict2, dict3):
            dict.update(d)

        logger.info("After concatenating :")
        logger.info(dict)
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    concatenate()    