# question4.py
# program to draw functions
# author: smxdip001


import math
function = input("Enter a function f(x):\n")

for y in range(-10,11): #range
    for x in range(-10,11): #domain
        yreal = -y 
        a = round(eval(function)) #calculate the y value for the corresponding x value
        if x == 0 and yreal == 0 and a != 0: #check if x and y are equal and if there is no intercept at 0.
            print("+",end="")
        elif x == 0 and a != yreal: # print vertical axis
            print("|",end="")
        elif yreal == 0 and a != 0: #print horizontal axis
            print("-",end="")
        elif a == yreal:
            print("o",end="")
        
        else:
            print(" ",end="")
        
    print()
        
               

    