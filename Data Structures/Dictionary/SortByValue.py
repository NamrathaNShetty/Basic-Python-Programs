'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 12:28  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 12:52
* @Title: To sort (ascending and descending) a dictionary by value
'''

from Loggers import logger

def sort_by_value():
    '''
    Description:
        This function used to sort the values in dictionary
        by ascending and descending order. 
    '''
    
    try:
        
        x = {'a': 2,'b': 1,'c': 3, 'd': 5,'e': 4 }

        logger.info("Sort by Ascending Order")
        logger.info(sorted(x.values()))

        logger.info("Sort by Descending Order")
        logger.info(sorted(x.values(), reverse= True))
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    sort_by_value()