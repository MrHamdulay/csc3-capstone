"""Program to draw graphs
Shane Robinson
17 April 2014"""

import math
print("Enter a function f(x):")
func = input()

def graph():
    yinc = 2/40
    for y in range(-10,11):
        for x in range(-10,11):
            x_point = x
            y_point = -y
            if x_point==0 and y_point==0 and round(eval(func))!=y_point:
                print("+",end="")
            elif x_point==0 and round(eval(func))!=y_point:
                print("|",end="")
            elif y_point==0 and round(eval(func))!=0:
                print("-",end="")
            elif y_point-yinc<=round(eval(func))<=y_point+yinc:
                print("o",end="")
            else:
                print(" ",end="")
        print()

graph()