'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 14:58
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 15:24
* @Title: Python function that takes two lists and returns True if they have at
least one common member.
'''

from Loggers import logger

def common_member(list1, list2):
    '''
    Description:
        This function Takes two lists and returns True 
        if they have at least one common member 
    Parameter:
        it takes list1,list2 2 parameters. 
    Return:
        it returns true. 
    '''
    try:
        result = False
        for x in list1:
            for y in list2:
                if x == y:
                    result = True
                    return result
    
    except Exception:
        logger.error("Invalid Input")

list1 = [1,2,3,4,5,6]
list2 = [1,2,7,8,9]
list3 = [7,8,9]
logger.info(common_member(list1, list2))
logger.info(common_member(list1, list3))

if __name__ == "__main__":
 common_member(list1,list2)

