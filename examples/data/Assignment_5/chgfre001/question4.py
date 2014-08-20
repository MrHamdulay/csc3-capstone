#a program to draw a text based graph of f(x)
#by frederick chigwaza
#15 april 2014

import math 
def grap():
    fx=input('Enter a function f(x):\n')
    x=0
    y=0
#defining the range of the axes    
    for x_axis in range(10,-11,-1):
        for y_axis in range(-10,11,1):
            x=y_axis
            roundfx= round(eval(fx))
            
#plotting points when x=rounded value of y
            if roundfx==x_axis:
                print('o', end='')
#defining the origin
            if y_axis==0 and x_axis==0 and not x_axis==roundfx:
                print('+', end='')

#defining the y axis
            if y_axis==0 and x_axis!=0 and not x_axis==roundfx:
                print('|', end='')
#defining the x axis
            if x_axis==0 and y_axis!=0 and not x_axis==roundfx:
                                print('-', end='')                
#printing a space where x is not equal to y
            else:
                if x_axis!=0:
                    if y_axis!=0:
                        if x_axis!=roundfx:
                            print(' ', end='')
                            
                            
        print()

grap()     