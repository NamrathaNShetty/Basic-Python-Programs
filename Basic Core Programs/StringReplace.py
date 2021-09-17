'''
* @Author: Namratha N Shetty
* @Date: 2021-09-08 15:28  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-08 15:28
* @Title: User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

import re 

str = "Hello <<UserName>>, How are you?"

# Userinput for the name.
name = input("Please enter your name: ")

# Checking if length of name is greater or equal to 3.
if re.match("^[A-Z]{1}[a-z]{2,}$", name):
    new_str = str.replace('<<UserName>>', name )
    print(new_str)
else:
    print("Enter a valid name")