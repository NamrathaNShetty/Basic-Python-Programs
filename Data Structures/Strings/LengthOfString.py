'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 13:04  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:15
* @Title: Program to calculate the length of a string.
'''

from Loggers import logger

def length():
    """
    Description: 
        This function is to find the length of string.
    """
    try:
        string = "Length"
        logger.info("The length of string is")
        logger.info(len(string))

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    length()