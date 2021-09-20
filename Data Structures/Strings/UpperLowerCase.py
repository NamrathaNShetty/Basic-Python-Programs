'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 13:46  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:57
* @Title: Python script that takes input from the user and displays that input back in
upper and lower cases.
'''
from Loggers import logger

try:
    
    string = input("Enter the String :")

    logger.info(string.upper())
    logger.info(string.lower())

except Exception:
    logger.error("Invalid Input")