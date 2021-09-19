'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 18:23  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 18:45
* @Title: Program to print all unique values in a dictionary.
'''
from Loggers import logger

def unique_values():
    '''
    Description:
        This function prints unique values in a dictionary
    '''
    try:
       
        data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        print("Original List: ",data)
        # Using set() + values() + dictionary comprehension
        # Get Unique values from list of dictionary
        u_value = set( val for dic in data for val in dic.values())
        print("Unique Values: ",u_value)

        logger.info("The unique values in list are : " + str(u_value))
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    unique_values()