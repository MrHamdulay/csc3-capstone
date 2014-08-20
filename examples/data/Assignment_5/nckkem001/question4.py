"""Program to graph functions textually in python
Kemeshan Naicker
16 April 2014"""

import math

def Graph_Function():
    function = input("Enter a function f(x):\n")
    yinc = 1/2
    for y in range(-10,11):
        for x in range(-10,11):
            y_real = -y
            if y_real - yinc <= eval(function) <= y_real + yinc:
                print("o",end="")
            elif x==0 and y_real==0:
                print("+",end="")        
            elif y_real==0:
                print("-",end="")
            elif x==0:
                print("|",end="")
            else:
                print(" ",end="")
        print()
            
Graph_Function()

    
        
