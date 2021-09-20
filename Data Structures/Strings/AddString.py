'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 13:32  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:45
* @Title: ython program to add 'ing' at the end of a given string (length should be at
least 3).If the given string already ends with 'ing' then add 'ly' instead
'''

from Loggers import logger

def add_string(str):
    '''
    Description:
        This function Add 'ing' at the end of a given string 
        (length should be at least 3). If the given string already 
        ends with 'ing' then add 'ly' instead. If the string length 
        of the given string is less than 3, leave it unchanged.
    Parameter:
        function takes str as parameter
    Returns:
        function returns str
    '''

    length = len(str)

    if length > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'
    return str

try:

    logger.info(add_string('collection'))
    logger.info(add_string('add'))
    logger.info(add_string('string'))

except Exception:
        logger.error("Invalid Input")