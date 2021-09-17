'''
* @Author: Namratha N Shetty
* @Date: 2021-09-08 15:28  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-08 15:28
* @Title: Flip Coin and print percentage of Heads and Tails
'''

import array
import logging
from Loggers import logger

def display(myArray):
    '''
    Description:
        This function is implemented to display the array
    Parameter:
        myArray to iterate the elements and to access the Array elements 
    '''
    try:
        for i in range(len(myArray)):
            print(myArray[i])
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    try:
        myArray = array.array("i",[11,12,15,18,27])
        display(myArray)
    except Exception:
        logger.error("Invalid")