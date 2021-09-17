'''
* @Author: Namratha N Shetty
* @Date: 2021-09-12 15:28  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-12 15:28
* @Title: To simulate stopwatch program
'''


import time
try:
    while True:
        #print("Enter 1 to Start Time:");
        start = int(input("Enter 1 to Start:"))
        startTime = time.time()
        #print("Enter 0 to Stop Time:")
        stop = int(input("Enter 0 to Stop Time:"))
        endTime = time.time()
        timeElapsed = endTime - startTime
        print("Time elapsed from Start to Stop is: ",timeElapsed, " Sec");
except ValueError:
    print("Invalid input ")