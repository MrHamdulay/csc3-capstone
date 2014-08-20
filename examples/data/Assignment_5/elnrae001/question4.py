'''Program to draw the graph of a function
Author:Raees Eland
Date:15 April 2014'''
import math
#prompts user for function
f=input('Enter a function f(x):\n')
inc=1/2
#Draws graph from inputed function
for y in range(10,-11,-1):
    for x in range(-10,11):
        y_value=eval(f)
        if y-inc<=y_value<=y+inc:
            print('o',end='')
        elif x==0 and y==0:
            print('+',end='')
        elif x==0:
            print('|',end='')
        elif y==0:
            print('-',end='')
        else:
            print(' ',end='')
    print()
            