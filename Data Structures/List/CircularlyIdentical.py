'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 16:05
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 16:18
* @Title: Program to check whether two lists are circularly identical.
'''
from Loggers import logger

def circularly_identical():
    """
    Description: Function two check whether two lists are circularly idnetical.
    """

    try:

        list1 = [10, 10, 0, 0, 10]
        list2 = [10, 10, 10, 0, 0]
        list3 = [1, 10, 10, 0, 0]

        logger.info('Compare list1 and list2')
        logger.info(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))   
    
        logger.info('Compare list1 and list3')
        logger.info(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
 circularly_identical()        