'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 16:20
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 16:30
* @Title: Program to split a list based on first character of word.
'''
from Loggers import logger

def split():
    '''
    Description:
         This function Splits a list based on first character of word
    '''
    try:
        
        list1 = ['Split', 'list', 'based', 'on', 'first', 'character', 'word']
        # creating the list of just the first character in each item of the list
        list2 = [item[0] for item in list1]
        logger.info(list2)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
 split()