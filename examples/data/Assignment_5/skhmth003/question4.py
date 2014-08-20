#This is a program for drawing graphs
#Author: Gordon Skhosana
#Date: 12/04/2014

import math

def graph():
    function=input("Enter a function f(x):\n")
    for y in range(10,-11,-1):
        for x in range(-10,11):
            #y value of funtion
            function_value_at_x=eval(function)
            if y-0.5<=function_value_at_x<=y+0.5:
                print ("o",end="")
            elif x==0 and y==0:
                print ("+",end="")            
            elif x == 0:
                print ("|",end="")
            elif y == 0:
                print ("-",end="")
            else:
                print (" ",end="")               
        print()
graph()    