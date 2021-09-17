'''
* @Author: Namratha N Shetty
* @Date: 2021-09-08 15:28  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-12 15:28
* @Title: To find the Euclidean distance
'''

import math

x = float(input("Enter the X Co-ordinate:"))  # X Co-ordinate
y = float(input("Enter the Y Co-ordinate:"))  # Y Co-ordinate
distance = math.sqrt(x*x + y*y)  # Applying the distance formula of Euclidean
print(" The Euclidean Distance from origin '",x,"' and '",y,"' is '",distance,"'")