''' Assignment 5 Question 4
Matshepo Malatji
15 April 2014'''

import math

#receive input from the user: the value of f(x)
function = input("Enter a function f(x):\n") #mx + c

#define a function that will draw the graph of f(x)
#retrieve the equation as a parameter

def f_graph(function):
#for every co-ordinate within the given boundaries determine the value of the function at that point
#if the (rounded) value of f(x) is equal to the y, output "o", else print the space or axis
    
    for y in range(10,-11,-1):
        for x in range(-10,11):
            value = eval(function)
            if round(value,0) == y:
                print('o', end ='')            
            elif x == 0 and y == 0: 
                print('+', end ='')
            elif x == 0: 
                print('|',end='')
            elif y==0 : 
                print('-',end ='')

            else:
                print(' ',end='')
        print()

f_graph(function)