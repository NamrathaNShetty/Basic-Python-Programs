'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 19:52  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 20:12
* @Title: Program to count the values associated with key in a
dictionary
'''

from Loggers import logger

def count_values():
    '''
    Description: 
        This function counts the values associated with key
    '''
    try:

        student = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]
    
        logger.info(sum(d['id'] for d in student))
    
        logger.info(sum(d['success'] for d in student))
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    count_values()