'''
* @Author: Namratha N Shetty
* @Date: 2021-09-19 01:17 
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-19 01:25
* @Title: Program to use of frozensets.
'''

from Loggers import logger

def frozen_set():
    '''
    Description:
        This function implements frozen set uses
    '''
    # Frozensets
    # initialize A, B and C
    A = frozenset([1, 2, 3, 4])
    B = frozenset([3, 4, 5, 6])
    C = frozenset([5, 6])

    #use isdisjoint(). Return True if the set has no elements in common with other. 
    logger.info(A.isdisjoint(C))  

    # issubset() method. Return True if the C has elements which are in B
    logger.info(C.issubset(B))  

    # issuperset() method. Return True if all the elements of C should be in B
    logger.info(B.issuperset(C))  

if __name__ == "__main__":
    frozen_set() 