'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 14:10 
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 14:21
* @Title: Python program to reverse a string.
'''

from Loggers import logger

def reverse():
    '''
    Description:
        This function reverses a string
    '''
    try:
    
        string1 = "Namratha"
        string = string1[::-1]
        logger.info("Reversed String is")  
        logger.info(string)
    
    except Exception:
        logger.error("Invalid Input") 

reverse()