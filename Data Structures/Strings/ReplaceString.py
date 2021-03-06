'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 13:20  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:30
* @Title: Program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
'''

from Loggers import logger

def change_char():
    '''
    Description:
        Get a string from a given string where all occurrences 
        of its first char have been changed to '$'
    '''
    try:
        
        str = "restart"
        char = str[0]
        
        logger.info("Before Replacing")
        logger.info(str)
        
        str1 = str.replace(char, '$')
        str1 = char + str1[1:]

        logger.info("After Replacing")
        logger.info(str1)

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
 change_char()