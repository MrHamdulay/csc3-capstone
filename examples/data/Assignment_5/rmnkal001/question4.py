#sketching amazing graphs.
#Kalind Ramnarayan
#15 April 2014
import math


function=input("Enter a function f(x):\n")# user inputs the formula of a function

def graph():
    for y in range(10,-11,-1):
        for x in range(-10,11):
            if y==round(eval(function)):    #plot the points of a function
                print("o",end="")            
            elif x==0 and y==0:             #plot the point where the x-axis meets the y-axis
                print("+",end="")
            elif x==0:                      #plot the y-axis
                print("|",end="")           
            elif y==0:                      #plot the x-axis
                print("-",end="")
            else:                           #plot the gap or empty spaces
                print(" ",end="")                  
        print()
                
                
graph()

#I did it yes yes!!!!