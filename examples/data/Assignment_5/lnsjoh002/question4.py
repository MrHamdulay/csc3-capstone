function = input("Enter a function f(x):\n")

import math

for y in range(10,-11,-1):
    if y!=10:
        print("")
    
    for x in range(-10,11):
        function_value = eval(function)
        function_value = round(function_value)
        if y == function_value:
            print('o',end="")
        
        elif x == 0 and y ==0:
            print('+', end="")
        elif x==0:
            print('|', end="")
        elif y==0:
            print('-', end="")
        else: print(" ", end="")
        
    
