'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 14:10 
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 14:21
* @Title: Python program to count occurrences of a substring in a string.
'''

from Loggers import logger

def occurence():
 """
  Description: this function helps to count occurrences of a substring in a string.
"""
 try:
    str1 = 'Is it the right time to talk to you'
    logger.info(str1.count("to"))
    
 except Exception:
    logger.error()

if __name__ == "__main__":
    occurence()