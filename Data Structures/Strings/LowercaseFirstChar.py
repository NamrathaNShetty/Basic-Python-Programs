'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 15:02 
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 15:21
* @Title: Python program to lowercase first n characters in a string.
'''
from Loggers import logger

def lower():
 """
 Description: Function to make lowercase first n characters in a string.
"""
 try:

    str1 = 'KARNATAKA'
    logger.info(str1[:4].lower() + str1[4:])

 except Exception:
    logger.error("Invalid Input")

if __name__ == "__main__":
    lower()    