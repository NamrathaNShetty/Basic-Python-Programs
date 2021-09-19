'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 18:52  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 19:12
* @Title: Program to create a dictionary from a string.
'''

from Loggers import logger
from collections import defaultdict, Counter

def create_string_Dict():
    '''
    Description:
        This function to create a dictionary from a string
    '''
    
    try:
        str1 = 'w3resource' 
        my_dict = {}
        
        for letter in str1:
            my_dict[letter] = my_dict.get(letter, 0) + 1
        
        logger.info(my_dict)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    create_string_Dict()