"""A5Q4 - Simple grapher
Keegan Crankshaw
15/4/2014"""

import math

def main():
    #ask the user for a function
    function = input("Enter a function f(x):\n")
    graph(function)

def graph(function):
    for y in range (10,-11,-1):
        for x in range (-10, 11):
            y_val = eval(function) #calculate the y-value
            #is the calculated value matches a current point
            if round(y_val) == y:
                print("o", end="")
            #draw the origin
            elif x==0 and y==0:
                print ("+",end="")            
            #draw the y-axis
            elif x == 0:
                print ("|",end="")
            #draw the x-axis
            elif y == 0:
                print ("-",end="") 
            #draw white space(no value/not a axis)
            else:
                print (" ",end="")
        print() #move onto the next line
        
if __name__ == "__main__":
    main ()