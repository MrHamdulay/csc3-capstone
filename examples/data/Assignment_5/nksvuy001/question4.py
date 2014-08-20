"""program to draw a text-based graph of a mathematical function f(x)
vuyolwethu nkosi
16 april"""

import math #first import math library so that math functions can be recognised
fox=input('Enter a function f(x):\n') #getting function from user
x=0 #initialising ie. making x the counter
#set ranges for grid of graph
for y in range(10,-11,-1): #y values act as our rows in graph grid. Also want python to read from bottom to top rather than other way round
    for x in range(-10,11,1): #x values act as our columns in graph grid
        if y==round(eval(fox)):
            print('o',end='') #where y=RHS of function is where you want the graph to print
        elif y!=0 and x==0:
            print('|',end='') #where the column is 0 and the row is not 0 it should print the y axis        
        elif y==0 and x!=0:
            print('-',end='') #where the row is 0 and the column is not 0 it should print the x axis 
        elif y==0 and x==0:
            print('+',end='') #where the y and x therefore row and column is 0, print origin
        else:
            print(' ',end='') #account for the spaces where there is no graoh drawn
    print()
            

            