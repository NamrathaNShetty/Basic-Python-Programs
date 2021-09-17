'''
* @Author: Namratha N Shetty
* @Date: 2021-09-17 23:45  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 24:58
* @Title: To remove the first occurrence of a specified element from an array
'''

from Loggers import logger

def delete_occurence(myArray, element):
    '''
    Description:
        This function removes the first occurence element 
        in an array.
    Parameter:
        It takes myArray and element to remove first occurence
    '''
    try:
        for i in range(len(myArray)):
            if myArray[i] == element:
                myArray.remove(element)
                break
        print("Array after removing", element, ' is', myArray)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    try:
        arr = [1,2,3,4,5,3,7,3,8,3]
        element = 3
        delete_occurence(arr, element)
    
    except Exception as e:
        logger.error(e)
            