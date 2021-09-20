'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 08:56  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 09:10
* @Title: Program to create the colon of a tuple.
'''
from Loggers import logger
from copy import deepcopy

try:

    tuple1 = (1, 2, 3.4, 'abc')

    tuple2 = deepcopy(tuple1)
    logger.info(tuple2)

except Exception:
    logger.error("Invalid")