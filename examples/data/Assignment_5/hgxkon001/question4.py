#question4 Assignment 5
#Konrad Hugo HGXKON001

import math
func = input("Enter a function f(x):\n")
graph = ''
#Program that plots an inserted function in range 10,-10
for y in range(10,-11,-1): #
    for x in range(-10,11):
        if round(eval(func))==y:# Actually draws the function if function inserted = y
            graph+='o'
        elif x ==0 and y == 0: #Plots the origin
            graph += '+'
        elif x == 0 and y != 0:
            graph+='|'      #Draws the Y-axis
        elif y == 0 and x != 0:
            graph += '-'    #Draws the X-axis
        else: 
            graph+=' ' #if not origin, or intercept, print a blank
    print(graph)
    graph = ''
        