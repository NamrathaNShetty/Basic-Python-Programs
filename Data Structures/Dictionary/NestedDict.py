'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 20:15  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 20:30
* @Title: Program to convert a list into a nested dictionary of keys.
'''

from Loggers import logger

def convert_to_dictionary():
    '''
    Description:
        This function converts list into nested
        dictionary of keys
    '''
    num_list = [1, 2, 3, 4]
    new_dict = current = {}
    
    for name in num_list:
        current[name] = {}
        current = current[name]
    
    logger.info(new_dict)

if __name__ == "__main__":
    convert_to_dictionary()