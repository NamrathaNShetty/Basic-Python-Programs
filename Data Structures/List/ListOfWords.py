'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 14:36
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 14:49
* @Title: Python program to find the list of words that are longer than n from a
given list of words.
'''
from Loggers import logger

def long_words():
    '''
    Description:
        This function Find the list of words that are longer
        than n from a given list of words
    '''
    try:

        str = "Find the list of words that are longer than n from a given list of words"
        n = int(input("Enter the length"))
        word_len = []
        txt = str.split(" ")
        
        for x in txt:
            if len(x) > n:
                word_len.append(x)
        
        logger.info(word_len)
    
    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
 long_words()
