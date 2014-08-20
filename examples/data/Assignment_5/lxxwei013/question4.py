"""Program to draw mathematical functions
Michelle Lu
15 April 2014"""

import math

def graph():
    function=input("Enter a function f(x):\n")
    for y in range(10, -11, -1):
        for x in range(-10,11):
            function_value=round(eval(function)) #rounds and computes function value
            if x==0 and y==0 and y!=function_value:
                print("+", end="") #origin
            elif y==function_value:
                print("o", end="")
            elif x==0 and y!=0 :
                print("|", end="") #y-axis
            elif y==0 and x!=0 :
                print("-", end="") #x-axis
            else: 
                print(" ", end="")
        print()
                
graph()