'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 13:04  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:15
* @Title: Program to count the number of characters (character frequency) in a
string.
'''

from Loggers import logger

def count():
    '''
    Description:
        Count the number of characters (character frequency) in a string
    Parameter:
        string1 is parameter.
    
    '''
    try:

        string1 = "google.com"
        dict = {}
        
        for n in string1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        
        logger.info(dict)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    count()