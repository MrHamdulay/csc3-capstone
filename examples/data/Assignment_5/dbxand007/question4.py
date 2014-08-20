"""Cherise Dube
14 April 2014
Program to draw any function given by a user between -10 and 10 on both axes"""

import math


function=input("Enter a function f(x):\n")
for y in range(-10,11):
    for i in range(-10,11):
        x=eval(function.replace('x','i'))
        if y==x:
            print ("o")
        
        elif y==0 and -10<=x<=10:
            print("-")
        
        elif x==0 and -10<=y<=10:
            print ("|")
        
        else:
            print(" ")
    print()
