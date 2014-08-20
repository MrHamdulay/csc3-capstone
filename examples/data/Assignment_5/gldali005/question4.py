# a program to draw a text-based graph of a mathematical function f(x).
# Ali Goldstein
# 16 April 2014

#prompt the user to enter a function
function = input("Enter a function f(x):\n")

#import math to get methods from the math library
import math

#drawing the function
#the axis iimits of (10.10) are the boundary for the range 
for y in range(-10,11):
    for x in range (-10,11):
        newY = -y
        if round(eval(function)) == newY:
            print("o", end = "")
        elif newY == 0 and x!=0:
            print("-",end = "")
        elif x == 0 and y!=0:
            print("|", end = "")  
        elif ((x==0) and (newY==0)):
            print("+",end = "")
        else: 
            print(" ",end = "")
    print("")
            
    
        
              
            
    