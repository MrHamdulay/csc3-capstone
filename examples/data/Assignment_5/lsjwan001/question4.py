# Program draws any given function
# Wandile Lesejane
# 16 April 2014 
import math

func=input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x in range(-10,11):
        funct=round(eval(func))
        if funct==y:
            print('o',end="")
        elif x==0 and y==0:
            print('+',end="")
        elif y==0:
            print('-',end="")
        elif x==0:
            print('|',end="")
        else:
            print(" ",end="")
    print()
        
    