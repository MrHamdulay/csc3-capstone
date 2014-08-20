# question4.py
# camilla craven
# 16 April 2014
# program to draw graph

import math # imports maths library

graph = input("Enter a function f(x):\n") # user inputs graph

for y in range(10,-11,-1): # creating length of y axis
    if y != 10:
        print()
    
    for x in range(-10,11): # creating length of x axis
        value = eval(graph) # change string into number
        value = round(value)  # round values of function
        
        if y == value: # y value exists
            print("o",end = "")
        
        elif x == 0 and y == 0: # creating spot where x axis meets y axis
            print("+", end = "") 
        elif x == 0: # creating y axis
            print("|", end = "")
        elif y == 0: # creating x axis
            print("-", end = "")
        else: print(" ", end = "")