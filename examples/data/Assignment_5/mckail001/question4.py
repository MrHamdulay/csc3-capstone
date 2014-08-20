#Ailsa Mackay: MCKAIL001
#Assignment 5 
#Question 1: Program to draw functions
#2014-04-16

import math #import math in the event that the user wants to draw trig functions

graph = ""
function = input('Enter a function f(x):\n') #user inputs a function

for y in range(10,-11,-1): #y loop must run backwards to acount for positive y values being at the top of the cartesian plain and negative y values being at the bottom
    for x in range(-10,11):
        if round(eval(function))==y:
            graph+="o"
        elif y==0 and x!=0:
            graph += "-" #for x-axis
        elif y==0 and x==0: 
            graph+="+" #for origin
        elif x==0 and y!=0:
            graph+="|" #for y-axis
        else: graph+=" "
    print(graph)
    graph=""
    #print graph and starts over as ''