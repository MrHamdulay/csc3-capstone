"""program to draw the graph of a given function
Runako muzwidzwa
15 April 2014"""

import math#to use math function
function=input("Enter a function f(x):\n")
for y in range(-10,11):#x axis values of x
    for x in range(-10,11):#y axis values of y
        #x=str(x_value)
        #f1=function.replace("x",x)#replaces the x with whatever value y_value is
        f=eval(function)#the function is evaluated because x is in the function you input
        f2=-round(f) 
        if y==0 and f2==0: #to ensure that if the function goes through the origin the point is plotted
            print("o",end="")
        elif y==0 and x==0:
            print("+",end="")
        elif y==f2:
            print("o",end="")
        elif y==0:
            print("-",end="")
        elif x==0:
            print("|",end="")
        else :print(" ",end="")

    print()