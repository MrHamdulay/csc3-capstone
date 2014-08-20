""" Print a graph of a function using ASCII art """
__author__ = 'Stephen Temple - TMPSTE002'
__date__ = '2014/04/13'

import math

# set x axis range and increment
X_MIN = -10
X_MAX = 10
X_INC = 1
x_multiplier = int(1 / X_INC)  # required if increment is a floating point number to convert to whole number

# set y axis range and increment
Y_MIN = -10
Y_MAX = 10
Y_INC = 1
y_multiplier = int(1 / Y_INC)  # required if increment is a floating point number to convert to whole number

function = input("Enter a function f(x):\n")
# iterate through each row, y axis
for y in range(int(y_multiplier*Y_MAX), int(y_multiplier*(Y_MIN-Y_INC)), int(-y_multiplier*Y_INC)):
    y /= y_multiplier   # convert back to floating point
    # iterate through each column, x axis
    for x in range(int(x_multiplier*X_MIN), int(x_multiplier*X_MAX+X_INC), int(x_multiplier*X_INC)):
        x /= x_multiplier  # convert back to floating point
        if eval(function) - (Y_INC / 2) < y < eval(function) + (Y_INC / 2):  # where y = x (within bounds)
            print('o', end='')
        elif x == 0 and y == 0:  # point of origin
            print('+', end='')
        elif x == 0:
            print('|', end='')  # y-axis
        elif y == 0:
            print('-', end='')  # x-axis
        else:
            print(' ', end='')  # need a space character to fill empty space on graph
    print()