'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 17:35  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 17:54
* @Title: To generate and print a dictionary that contains a number (between 1 and n)
 in the form (x, x*x).
'''

from Loggers import logger

def power_Dict():
    '''
    Description:
        This function to generate and print a dictionary that 
        contains a number (between 1 and n) in the form (x, x*x).
    '''
    
    try:
        n=int(input("Input a number ")) 
        d = dict()

        for x in range(1,n+1):
            d[x]=x*x
        print(d)
        logger.info(d)

    except ValueError:
        logger.error("Invalid input")

if __name__ == "__main__":
    power_Dict()