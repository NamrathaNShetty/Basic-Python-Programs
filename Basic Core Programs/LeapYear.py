'''
* @Author: Namratha N Shetty
* @Date: 2021-09-10 10:08  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-10 10:08
* @Title: To check for leap year
'''
import re

Year = input("Enter a year to check: ")

# Condition to check for valid year.
if re.match("^[0-9]{4}$", Year):

    if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)): 
        print(" Its a leap year")
    else:
        print("Its not a leap year")

else:
    print("Enter a valid year")