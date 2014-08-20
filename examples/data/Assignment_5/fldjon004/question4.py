# question4.py
# jono field
# 16 april 2014
# program to draw graph


function = input("Enter a function f(x):\n") # prompts user for function of choice
import math # imports math library
for y in range(10,-11,-1): # y axis from -10 to 10
    if y!=10:
        print("")
    
    for x in range(-10,11): # x axis from -10 to 10
        function_value = eval(function)
        function_value = round(function_value) 
        if y == function_value:
            print('o',end="")
        
        elif x == 0 and y ==0: # creating middle where x axis meets y axis
            print('+', end="")
        elif x==0: # creating y axis
            print('|', end="")
        elif y==0: # creating x axis
            print('-', end="")
        else: print(" ", end="")

        

        
        
        
        
