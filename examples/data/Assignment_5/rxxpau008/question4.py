#Description: Draws graphs of functions entered between -10 and 10
#Name: Paul Roux - RXXPAU008
#Date: 15 April 2014

import math

f = input("Enter a function f(x):\n")
values = []

for x in range(-10,11,1):#Gets all the values of the function between -10 and 10
    values.append((x,round(eval(f))))
    
    
for y in range(10,-11,-1):#Uses the values from the function to draw the graph
    for x in range (-10,11,1):
        if (x,y) in values:
            print("o",end="")
        elif x==0 and y==0: print("+",end="")
        elif y==0: print("-",end="")
        elif x==0: print("|",end="")
        else: print(" ",end="")
    print()
        
    