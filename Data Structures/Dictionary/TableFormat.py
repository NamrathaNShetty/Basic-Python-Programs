'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 18:52  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 19:12
* @Title: Program to print a dictionary in table format.
'''

from Loggers import logger

def table_format():
    '''
    Description:
        This function to print a dictionary in table format
    '''
    
    try:
        # Define the dictionary
        dict ={}

        # Insert data into dicitonary
        dict1 = {1: ["Samuel", 21, 'Data Structures'],
	        2: ["Richie", 20, 'Machine Learning'],
	        3: ["Lauren", 21, 'OOPS with java'],
	    }

        #Print name of columns
        logger.info("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

        # print each data item.
        for key, value in dict1.items():
	        name, age, course = value
	        logger.info("{:<10} {:<10} {:<10}".format(name, age, course))
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    table_format()