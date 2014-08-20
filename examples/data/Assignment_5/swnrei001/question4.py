''' ASCII graph plotter
Author: SWNREI001
Date: 2014-04-14'''

import math

def GetValueFrom(x, func):
    '''Evaluate function 'func' with x replaced for the supplied x value'''
    return eval(func.replace('x', "(" + str(x) + ")"))

def Plot(func):
    for y in range(21):
        for x in range(21):
            rect_x = x - 10 # rectified x value
            rect_y = -(y - 10) # rectified y value
            y_needed = round(GetValueFrom(rect_x, func))
            if rect_y == y_needed:
                print("o", end = "")
            elif rect_x == rect_y == 0:
                print("+", end = "")
            elif rect_x == 0:
                print("|",end="")
            elif rect_y == 0:
                print("-",end="")
            else:
                print(" ",end="")
        print()    

if __name__ == '__main__':
    function = input("Enter a function f(x):\n")
    Plot(function)