#Nikhil Jiten Naik
#Comsci 1015F
#Assignment 5

import math

fx = input("Enter a function f(x):")
for y in range(10,-11,-1):
    print()
    for x in range(-10,11,1):
        coordinate = round(eval(fx))
        
        if coordinate == y:
            print("o", end="")
            
        else:
            if x==0 and y==0:
                print("+", end="")
            elif x==0:
                print("|", end="")
            elif y==0:
                print("-",end="")
            else:
                print(" ",end="")
            
        
        

