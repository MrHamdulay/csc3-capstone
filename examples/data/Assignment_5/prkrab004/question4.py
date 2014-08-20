#Assignment 5
#Question 4
#Rabia Parker
#Due Date: 17/04/2014

import math

def text_based_graph():
    graph=input("Enter a function f(x):\n") #get function
    x=0
    y=0
    
    for y_axis in range(10,-11,-1): #y co-ordinates
        for x_axis in range(-10,11,1): #x co-ordiantes
            x=x_axis
            point=round(eval(graph)) #round off points for graph
            if point == y_axis:
                print("o",end="")
            if y_axis == 0 and x_axis == 0 and not x_axis == point: #plot point (0,0)
                print('+',end='')
            if x_axis == 0 and not y_axis == 0 and not y_axis == point: #draw y-axis
                print('|', end='')
            if y_axis == 0 and not x_axis == 0 and not y_axis == point: #draw a-axis
                print('-', end='')
            else:
                if not y_axis == 0:
                    if not x_axis == 0:
                        if not y_axis == point:
                            print(' ', end='')
        print()
text_based_graph()
            
            
    
  
        


