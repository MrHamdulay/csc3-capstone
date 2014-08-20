"""program to draw a text based graph of a mathematical function
Kristin Kinmont
13 April 2014"""

import math
#get the function
graph = input("Enter a function f(x):\n")

for y in range(-10,11):
    for x in range(-10,11):
        y_real = y*(-1) 
        #plot points
        if y_real == round(eval(graph)):
            print("o",end="")
        #Print origin    
        elif x==0 and y_real == 0:
            print("+",end="")
        #print y-axis
        elif x == 0:
            print("|",end="")
        #print y-axis
        elif y_real ==0:
            print("-",end="")
    
        else:
            print(" ",end="")

    print()