"""Program that draws a text based graph of a mathematiccal function, f(x), as given by the user"""

#Assignment 5 Question 4 2014/04/14
#Brandon Pickup

function = input("Enter a function f(x):\n")
import math
def functionValue(x):#definition acepts an x value
    y=eval(function)#sets y to the actual function supplied by the user after eval has been applied to the function
    return y#computes the function with the x value supplied as a parameter in the functionValue definition

for y in range(10,-11,-1):#runs through the y axis from top to bottom, with an axis ranging from -10 to 10. starts at 10 because we are working from the top down
    for x in range (-10,11,1):#runs through each x value on the scale -10 to 10 at each y value
        if y == round(functionValue(x)):print("o",end="")#if the functionValue at x, rounded, is the same as the current y position we are in. an 'o' is printed to represent a spot on the graph
        elif x==0 and y==0: print("+",end="")#prints a '+' to indicate where the x and y intercepts cross eachother
        elif x==0: print("|",end="")#uses '|' to draw the y axis
        elif y==0: print("-",end="")#uses '-' to draw the x axis wherever the y value for a particular iteration = 0
        else: print(" ",end="")#if the current x and y value are not a point on the graph, or an axis, a space is printed
    print()#jumps to the next line for the new y iteration of the loop
    
        