"""HELIN KIM!!!!!!!!!!!!!
graphing functions like a boss
17 April 2014"""
import math
function=input("Enter a function f(x): \n")

for y in range (10,-11,-1):
    for x in range (-10,11):
        num=round(eval(function))
        
        if y == num:
            print("o",end="")
        elif y == 0 and x == 0:
            print("+",end="")
        elif x == 0: 
            print("|",end="")
        elif y == 0:
            print("-",end="")
        
        else:
            print(" ",end="")
            
    
    print()
        
