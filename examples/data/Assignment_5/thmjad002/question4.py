"""Assignment 5, Question 4
Jadon Thomson
2014-04-14"""

import math


def graph_f():
    function = input("Enter a function f(x):\n")    
    for y in range (10,-11,-1):
        for x in range (-10,11):
            function_value = eval(function)
            function_value = round(function_value)
            if function_value == y:
                print("o",end='')
            elif x == 0 and y == 0:
                print("+",end='')
            elif x == 0:
                print("|",end='')
            elif y == 0:
                print("-",end='')
            else:
                print(" ",end='')
        print(" ")
    
graph_f()
