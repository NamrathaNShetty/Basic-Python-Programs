'''
* @Author: Namratha N Shetty
* @Date: 2021-09-08 15:28  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-08 15:28
* @Title: Flip Coin and print percentage of Heads and Tails
'''

import random

n = 0

def flipCoin():
    heads = 0  # track heads count
    tails = 0  # track tails count
    headspercent = 0  # heads percentage
    tailspercent = 0  # tails percentage
    n = int(input("How many times do you want to Flip Coin?"))
    if n >= 0:
        for i in range(n):  # run the experiment n times
            coin = random.randint(0, 1)  # assign a value to coin, either 0 or 1

            if coin == 0:  # if coin value is assigned as 0
                heads += 1  # increase heads count by 1
            else:  # if coin value is assigned something other than 1
                tails += 1  # increase tails count by 1

            # Calculating head and tail percentage
            headspercent = ((heads / (heads + tails)) * 100)  
            tailspercent = ((tails / (heads + tails)) * 100) 

        # Printing the values and converting numbers to string by str()
        print("Heads percent: " + str(headspercent)) 
        print("Tails percent: " + str(tailspercent))  
    else:
        print("Enter the positive Number:")

# Driver code

flipCoin()