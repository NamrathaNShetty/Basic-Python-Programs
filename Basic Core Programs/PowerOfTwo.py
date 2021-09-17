'''
* @Author: Namratha N Shetty
* @Date: 2021-09-08 15:28  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-08 15:28
* @Title: To print powers of two
'''
from math import pow

n= int(input("Enter the power of two :"))

# Checking if entered range is within the limit.
if(0<n<31):
    for i in range (n):      
        print("2 ^ ",i," = ",pow(2,i))
else:
    print("Enter the proper range")