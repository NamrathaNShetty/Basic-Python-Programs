'''
* @Author: Namratha N Shetty
* @Date: 2021-09-18 21:01  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-18 21:12
* @Title: Program to count number of items in a dictionary value
that is a list.
'''

from Loggers import logger

def count_number_items():
    '''
    Description:
        to count number of items in a dictionary value that is a list.
    '''
    
    dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    count = sum(map(len, dict.values()))
    logger.info(count)

    # using isinstance method and  in operator 
    count = 0
    for x in dict:
        if isinstance(dict[x], list):
            count += len(dict[x])
    print(count)

if __name__ == "__main__":
    count_number_items()