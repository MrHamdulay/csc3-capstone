#Program used to display the graph of a inputted function
#Keanon Fell
#15 April 2014

import math
function = input("Enter a function f(x):\n")#Entering the function so that the program can draw a visual of the function
for y in range(10,-11,-1):#Loop through every row
    for x in range(-10,11):#Loops through every 'column'
        coordinate = round(eval(function))
        #THe code to help you draw the axis and the points of the graph
        if x == 0 and y == 0 and y != coordinate:
            print("+",end="")
        if x == 0 and y !=0 and y != coordinate:
            print("|",end="")
        if y == 0 and y != coordinate and x != 0:
            print("-",end="")
        if y == coordinate:
            print("o",end="")
        else:#For the parts in the grid when there is no axxis or point print a blank space
            if y != 0:
                if x != 0:
                    if y != coordinate:
                        print(" ",end="")
    print()