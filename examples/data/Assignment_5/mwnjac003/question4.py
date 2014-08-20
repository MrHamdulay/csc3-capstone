# program to plot the graph of a function
# by Jacob Mwanza
# 14/04/2014

import math


#enter function

def plot_graph():
    function = input("Enter a function f(x):\n")
    for y_axis in range(10,-11,-1):
        for i in range(-10,11):
            x = i
            y = round(eval(function))
            
            # plot function values
            if y_axis == y:
                print ('o', end ='')
            elif y_axis == i == 0 and y!= 0:
                print('+',end='')
            elif y_axis == 0 and y != 0:
                print('-', end='')
            elif i == 0:
                print('|',end = '')
            else:
                print(' ',end ='')
        print()

plot_graph()