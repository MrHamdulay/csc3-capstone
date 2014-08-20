#Drawing a text based graph of f(x)
#By: Dean de Haast
#15 April 2014

import math

def main():
    #Enter a function
    function = input("Enter a function f(x):\n")
    x=0
    #Creating the grid
    for rows in range (10,-11,-1):
        for columns in range (-10,11):
            x=columns #Substituting each value into the equation. 
            rounded_function=round(eval(function))#Round the function
            
            if rounded_function == rows: #Plot the points
                print("o", end= "")
            #Creating the axes
            if rows == 0 and columns ==0 and rows != rounded_function: 
                print("+", end="")            
            elif rows == 0 and columns != 0 and rows != rounded_function:
                print("-", end="")
            elif columns == 0 and rows != 0 and rows != rounded_function:
                print("|", end= "")
            elif rows != 0 and columns != 0 and rows != rounded_function:
                print(" ", end="")
        print()
main()
            