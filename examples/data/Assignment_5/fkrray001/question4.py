# Author : Rayaan Fakier FKRRAY001
# Date : 15 - 04 - 2014
# Program which creates a user-defined graph

import math

def main():
    function = input("Enter a function f(x):\n")
    posx = function.find("x") # Find "x" to subs values in
    
    for rows in range(10,-11,-1): 
        for columns in range(-10,11):
            if posx != -1: # If the function has 'x'
                func_subs = function[:posx] +"("+ str(columns)+")"+ function[posx + 1:] # Subs x values in
                point = round(eval(func_subs)) # Produces y-values
            else:
                point = round(eval(function))
            # If - elif statements to create and plot the graph accordingly
            if rows !=0  and rows != point and columns != 0:
                print(" ",end="")
            elif rows != 0 and rows != point and columns == 0:
                print("|",end="")
            elif rows == 0 and rows != point and columns == 0:
                print("+",end="")
            elif rows == 0 and rows != point and columns != 0:
                print("-",end = "")
            elif rows == point:
                print("o",end="")                
        print()
          
main()