#Assignment 5
#Question 4
#16 April 2014
#Barry Su
#Program to draw a textbased graph of a mathematical function f(x)

import math

#define the function to draw the graph
def graph():
    fn = input("Enter a function f(x):\n")
    x = 0   #initiate the x value
    y = 0   #initiate the y value
    #create the graph using rows and columns
    #let row represent y-values and col represent x-values
    for row in range(10,-11,-1):
        for col in range(-10,11,1):
            x=col 
            round_y=round(eval(fn))#y value is a rounded value of the function
            if round_y==row:
                print("o", end="")
            elif col==0 and row!=0 and row!=round_y:
                print("|", end="")
            elif row==0 and col!=0 and row!=round_y:
                print("-", end="")
            elif row==0 and col==0 and row!=round_y:
                print("+", end="")            
            else:
                if row!=round_y:
                    if row!=0:
                        if col!=0:
                            print(" ", end="")
        print()

graph()