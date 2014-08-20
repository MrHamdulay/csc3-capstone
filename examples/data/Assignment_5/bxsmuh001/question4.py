#Assignment 5, Question 4
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 17/04/2014

#This program is designed to graph a given function f(x) in ASCII art. 

#Defining the function graphPlotter() to plot the graph
import math
def graphPlotter():
    #Pre-condition: Input function equation
    #Post-condition: Plot graph
    equation = input("Enter a function f(x):\n")
    x = 0 #Initializing value of x
    y = 0 #Initializing value of y

    for X in range(10,-11,-1):
        for Y in range(-10,11,1):
            x=Y
            coordinate = round(eval(equation)) #The equation makes use of x and is converted to an integer and rounded.
            
            #If the coordinate matches the value of X,a point is plotted.           
            if(coordinate == X):
                print("o", end="")
            
            #Prints the Origin.  
            if((X==0) and (Y==0) and (X != coordinate)):
                print("+", end="")
            
            #Prints the Y-Axis.
            if((Y == 0) and (not X == 0) and (X != coordinate)):
                print("|", end="")
            
            #Prints the positive and negative axes.
            if((X==0) and (not Y==0) and (X != coordinate)):
                print("-", end="")
                
            else:
                if(X != 0):
                    if(Y != 0):
                        if(X != coordinate):
                            print(" ", end="")
        print()

graphPlotter()