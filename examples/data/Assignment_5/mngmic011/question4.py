"""Micaela Menegaldo
question4
drawing a graph"""

import math

def axes(function):
    extra=0
    power='**'
    if len(function)>1 or 'x' not in function:
        extra=2*(eval(function[len(function)-1:len(function)]))
    if power in function:
        i=function.find('x')
        if i==0:
            extra=2*(eval(function[len(function)-1:len(function)]))
        else:
            extra=-2*(eval(function[len(function)-1:len(function)]))
    if 'sin' in function:
        extra=0
    for y in range (-10,11):
        for x in range (-10,11):
            func=function.replace('x','-x')
            y_value=round(eval(func))-extra
            x_value=x      
            if y==y_value:
                print("o",end="")
            elif x==0 and y==0:
                print("+",end="")
            elif x==0:
                print("|",end="")
            elif y==0:
                print("-",end="")
            elif y_value==y:
                print("o",end="")
            else:
                print(" ",end="")
        print()

if __name__=='__main__':
    function=input("Enter a function f(x):\n")
    axes(function)

    