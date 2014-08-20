""" Graph plotting program
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-14 """

import math

graph = ''
# Request a mathematical function from the user
func = input('Enter a function f(x):\n')

# Draw axes unless f(x) = y
for y in range(10,-11,-1):
    for x in range(-10,11):
        # Evaluate the function
        if round(eval(func)) == y:
            graph += 'o'
        elif (y == 0 and x != 0):
            graph += '-'
        elif y == 0 and x == 0:
            graph += '+'
        elif x == 0 and y!= 0:
            graph += '|'
        else: graph += ' '
    print(graph)
    graph=''