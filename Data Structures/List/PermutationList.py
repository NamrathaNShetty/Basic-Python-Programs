'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 15:45
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 16:02
* @Title: Python program to generate all permutations of a list in Python.
'''
from Loggers import logger
import itertools

def permuatation_comb():
   try:
    """
    Description: Function to generate all permutations of a list
    """
    list1 = [1, 2, 3]
    permutation = itertools.permutations(list1)
    list2 = list(permutation)
    logger.info(list2)

   except Exception as e:
    logger.error(e)

if __name__ == "__main__":
 permuatation_comb()