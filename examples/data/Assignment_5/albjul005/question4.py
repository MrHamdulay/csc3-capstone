""" Change calculating POS program
Julian Albert
ALBJUL005
15-04-2014"""

#imports math module
import math
#graph function starts as blank
graph = ''
function = input('Enter a function f(x):\n') #users input
#range of the inputed function
for y in range(10,-11,-1):
    for x in range(-10,11):
        if round(eval(function)) == y:
            graph += 'o'
        elif (y == 0 and x != 0):
            graph += '-' #sets x-axis
        elif y == 0 and x == 0: 
            graph += '+' #sets origin
        elif x == 0 and y!= 0:
            graph += '|' #sets y-axis
        else: graph += ' '
    print(graph)
    graph=''
    #print graph and starts over as ''