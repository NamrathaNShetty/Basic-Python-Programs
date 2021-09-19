'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 20:50  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 20:59
* @Title: Program to check multiple keys exists in a dictionary.
'''

from Loggers import logger

def multiple_keys():
    '''
    Description:
        This function to check multiple keys exists in a dictionary
    '''

    student = {
    'name': 'Alex',
    'class': 'V',
    'roll_id': '2'
    }
    
    logger.info(student.keys() >= {'class', 'name'})
    logger.info(student.keys() >= {'name', 'Alex'})
    logger.info(student.keys() >= {'roll_id', 'name'})

if __name__ == "__main__":
    multiple_keys()