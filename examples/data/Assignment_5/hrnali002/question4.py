# A program that draws mathamatical functions
# Alison Hoernle
# HRNALI002
# 13 April 2014

import math

# Get the input function that user enters
graph = input("Enter a function f(x):\n")

# create the outer loop for y going from -10 to 10
for y in range(-10, 11):

    # create the nested loop for x going from -10 to 10
    for x in range(-10, 11):
        
        value = round(eval(graph)) # only plot rounded values calculate the f values for all the x values in loop
        y_real = -y #want axis to go from positive to negative
        
        # All the conditions of what to plot to draw graph
        
        if x == 0 and y_real != 0 and value != y_real:
            print('|', end = '')
        elif y_real == 0 and x != 0 and value != 0:
            print('-', end = '')
        elif y_real == 0 and x == 0 and value != y_real:
            print('+', end = '')
        
        elif value == y_real:
            print('o', end = '')
        else: # value != y_real and value != 0 and y_real != 0:
            print(' ', end = '')
    
    # print a new line at the end of inner loop before next iteration of outer loop   
    print()
        
        
            
            