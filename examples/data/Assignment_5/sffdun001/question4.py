#Assignment 5- Question 4
#Duncan Saffy
#14-04-2014
import math
func=input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    
    for x in range(-10,11):
        
        if y==round((eval(func)),0):
            print("o",end="")        
        elif y==0 and x==0:
            print("+",end="")
            
        elif x==0:
            print("|",end="")
            
        elif y==0:
            print("-",end="")
            
        else:
            print(" ",end="")
    print()