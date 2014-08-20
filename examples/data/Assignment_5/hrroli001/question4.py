# Question 4 - Assignment 5
# Oliver Harrison
# 14 April 2014

# build area
# plot function
# create axis

import math

function=input("Enter a function f(x):\n")

"""function="x+2"
x=3
print(eval(function))"""

for y in range(10, -11, -1):
    for i in range (-10, 11):
        x=i
        #print(y, x, eval(function))
        if y==round(eval(function)):
            print("o", end="")
        elif i==0 and y==0:
            print("+", end="")
        elif i==0:
            print("|", end="")
        elif y==0:
            print("-", end="")
        
        else:
            print(" ", end="")
        #print("x", end="")
    print()
    


