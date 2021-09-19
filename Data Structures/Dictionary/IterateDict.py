'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 13:42  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 14:25
* @Title: Program to iterate over dictionaries using for loops.
'''

from Loggers import logger

def iterate_dictionary():

    '''
    Description:
        This function implemented iterate over dictionaries using for loops.
    '''

    dict1 = {'a': 'Chicken', 'b': 'Fish', 'c': 'Egg'}

    # Return keys or values explicitly
    for keys in dict1.keys():
        logger.info(keys)

     # Return keys or values explicitly
    for values in dict1.values():
        logger.info(values)

     # Return keys and values explicitly
    for key_values in dict1.items():
        logger.info(key_values)    

if __name__ == "__main__":
    iterate_dictionary()    