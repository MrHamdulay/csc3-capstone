"""Drawing a straight line graph on a grid by users input
Assignment 5
Nandani Birjanund
16/04/14"""

import math
function=input("Enter a function f(x):\n") #User inputs function
#Creates a grid for a function
for i in range(10,-11,-1):
    
    for j in range(-10,11):
        x = j
        y = round(eval(function))  #Rounds off what user has entered (conversion)
        if y == i:
#if values correspond (when the graph hits a point on the grid), print an empty circle(line of function)
            print("o", end = "")
        elif(j==0 and i == 0):
            print('+',end = '') #When the x and y axes intersect
        elif(i==0):
            print('-', end = '')        #for x-axis
        elif(j==0):
            print('|', end = '')    #for y-axis
        else:
            print(' ',end = '') #for all other places where the graph does not correspond with any of the above
        
            
    print()
#A straight line is printed 