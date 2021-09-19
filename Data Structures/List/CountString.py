'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 13:25  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 13:45
* @Title: Program to count the number of strings
'''

from Loggers import logger

def count_string():
    """
    Description: 
        This function is to count sting in list with lenght 2 or more 
        and same first and last letter.
    """
    
    try:
        str_list = (['abc', 'xyz', 'aba', '1221'])
        count = 0

        for word in str_list:
            if len(word) > 1 and word[0] == word[-1]:
                count += 1
        print("Number of strings where the string length is 2 or more and the first and last character is :", count)
        logger.info(count)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    count_string()