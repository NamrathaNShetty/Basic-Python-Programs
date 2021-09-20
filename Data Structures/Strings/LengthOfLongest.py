'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 13:32  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:45
* @Title: Python function that takes a list of words and returns the length of the longest
one.
'''
from Loggers import logger

def find_longest_word(words_list):
    '''
    Description:
        This function takes a list of words and
        return the length of the longest one.
    Parameter:
        takes words_list as parameter.
    Return:
        returns the length of the string.
    '''
    
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1]

result = find_longest_word(["Python", "Hive", "Frontend"])
logger.info("Length of the longest word: ")
logger.info(result[0])