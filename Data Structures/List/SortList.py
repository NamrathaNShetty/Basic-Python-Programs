'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 13:48 
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 14:05
* @Title: Program to print the list of tuple in increasing order keeping last value as key.
'''

from Loggers import logger

def last(num):
    '''
    Description:
        This function returns the last tuple items in the list
    Parameter:
        it takes num as parameter.
    Return:
        it returns the num
    ''' 
    return num[-1]

def sort_list_last(tuples):
    '''
    Description:
        This function returns the sorted tuple to the called function
    Parameter:
        it takes tuples as parameter
    Return:
        it return the sorted last tuple items.
    '''
    
    return sorted(tuples, key=last)

logger.info(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

