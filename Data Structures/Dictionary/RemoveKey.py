'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 17:35  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 17:54
* @Title: Program to remove a key from a dictionary.
'''
from Loggers import logger

def remove_key():
    '''
    Description:
        This function removes a key from a dictionary
    '''
    try:
    
        myDict = {'a':1, 'b':2,'c':3,'d':4, 'e':5 }
        print(myDict)
       
        #Delete method to remove key
        if 'a' in myDict: 
            del myDict['a'] 
            print(myDict)   
        logger.info(myDict)

        #Pop method to remove key
        removed_value = myDict.pop('e')
        print ("The removed key's value is : " + str(removed_value))
        print ("The dictionary after remove is : " + str(myDict))
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove_key()
