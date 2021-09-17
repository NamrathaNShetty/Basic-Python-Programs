'''
* @Author: Namratha N Shetty
* @Date: 2021-09-17 21:45  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-17 21:58
* @Title: Get the number of occurence of an element in an array
'''

from Loggers import logger

def occurences(myArray, element):
    '''
    Description:
        This function implemented to find the number of 
        occurence of an given number.
    Parameter:
        myArray and key takes to find the occurences. 
    '''
    
    try:
        count = 0
        
        for i in range(len(myArray)):
            if myArray[i] == element :
                count += 1 
        
        print('The Number of Occurences of', element ,'is: ' ,count,'times')

    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    
    try:
        arr = [1,2,3,7,5,3,7,3,8,3]
        element = 7
        occurences(arr, element)
    
    except Exception:
        logger.error("Invalid input")
