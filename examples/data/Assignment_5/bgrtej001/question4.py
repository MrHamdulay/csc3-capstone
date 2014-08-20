#Assignment 5, Question 4
#Graph plotter
#Tejasvin Bagirathi BGRTEJ001
#2014-04-17

import math

#User inputs function
func = input('Enter a function f(x):\n')

#Loop for y-axis
for y in range(-10, 11):
    #Loop for x-axis
    for x in range(-10, 11):
        #Invert y value
        y_real=-y
        #Create boundary for function value
        yinc=1/2
        #Invoke evaluate function, to convert from string
        fx = eval(func)
        #If function value is within range of y(created by y_inc) plot point
        if y_real - yinc <= fx <= y_real + yinc:
            print('o', end='')
        #Print x-axis
        elif y_real == 0 and x != 0:
            print('-', end = '')
        #Print '+' at (0;)
        elif y_real == 0 and x == 0:
            print('+', end='')
        #Print y-axis
        elif x == 0:
            print('|', end='')
        #Print space if func is insignificant
        else: print(' ', end='')
    print()