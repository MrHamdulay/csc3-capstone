""" program that graphs functions
kenneth mphele
201/04/16"""
import math
def function():
    f=input("Enter a function f(x):\n") 
    
    for y in range(10,-11,-1):
        for x in range(-10,11):
            a=round(eval(f))
            if y==a:
                print("o",end="")
            elif y==0 and x==0:
                print("+",end="")
            elif  y==0:
                print("-",end="")
            elif x==0:
                print("|",end="")
            else:
                print(" ",end="")
        print()
            
function()