'''
* @Author: Namratha N Shetty
* @Date: 2021-09-20 13:46  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 13:57
* @Title: Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
'''

from Loggers import logger

def sort():
    """
    Description:
        This function is to sort the comma separated value.
    """
    try:

        items = 'red, white, black, red, green, black'
        words = [word for word in items.split(",")]
        logger.info(",".join(sorted(list(set(words)))))
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    sort()