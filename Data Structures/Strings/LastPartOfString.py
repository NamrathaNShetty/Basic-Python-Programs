'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 13:59  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 14:15
* @Title: Python program to get the last part of a string before a specified character.
'''

from Loggers import logger

def split_string():
    """
    Description:
        This function to get the last part
         of a string before a specified character.
    """
    try:
        
        string = 'https://www.w3resource.com/python-exercises/string'
        string1= 'https://github.com/NamrathaNShetty/Basic-Python-Programs'
        logger.info(string.rsplit('/', 1)[0])
        logger.info(string.rsplit('-', 1)[0])
        logger.info(string1.rsplit('/', 1)[0])
        logger.info(string1.rsplit('-', 1)[0])

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    split_string()