'''  a program to draw a text-based graph of a mathematical function f(x)
     Phillip Ruhesi
     16 April 2014'''
import math
function=input('Enter a function f(x):\n')     #prompts user to enter function
for y in range(10,-11,-1):
    for x in range(-10,11):               
        if y==round(eval(function)):            #prints the points of the graph
            print('o',end='')
        elif y==0 and x==0:                     #prints symbol at center of the graph
            print('+',end='')
        elif y==0:
            print('-',end='')
        elif x==0:                              #prints a blank graph withtwo axes x and y
            print('|',end='')
        else:
            print(' ',end='')
    print()        