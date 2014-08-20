"""makes a graph
Adam Kaliski
CSC1015 Assignment 5"""
import math

function = input("Enter a function f(x):\n")

for y in range (10,-11,-1):
    for x in range (-10,11):
        val='('+str(x)+')'
        yval = eval(function.replace('x',val))
        if (y==round(yval)):
            print('o',end='')
        elif(x==0 and y==0):
            print('+',end='')
        elif(x==0):
            print('|',end='')
        elif(y==0):
            print('-',end='')
        else:
            print(' ',end='')      
    print()    
    