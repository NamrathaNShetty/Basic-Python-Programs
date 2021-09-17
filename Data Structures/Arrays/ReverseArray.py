'''
* @Author: Namratha N Shetty
* @Date: 2021-09-17 20:56  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-17 21:32
* @Title: Create and array and reverse the elemens
'''

from Loggers import logger

def reverse(arr):
    '''
    Description:
        This function reverse the elements of an array
    Parameter:
        arr to iterate the elements and reverse the elements
    '''

    #Loop through the array in reverse order    
    for i in range(len(arr)-1, -1, -1):     
        logger.info(arr[i])

if __name__ == "__main__":
    try:
        arr = [1, 2, 3, 4, 5];     
        logger.info("Original array: ");    
    
        for i in range(0, len(arr)):    
            logger.info(arr[i]),     
        
        logger.info("Array in reverse order: "); 
        #reverse(arr) 

    except Exception:
        logger.error("Invalid input")