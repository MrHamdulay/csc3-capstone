''' A program that draws a text-based graph of a mathematical function f(x)
Sandile Christopher Mahlangu
15 April 2014'''
import math

def f():
    '''This function prints a graph of f(x)'''
    function=input('Enter a function f(x):\n')
    for y in range(10,-11,-1):
        #Vertical Axis
        for x in range(-10,11):
            #Horizontal Axis
            f_x=round(eval(function))#calculates f(x) and rounds it off to no decimal places
            if y ==f_x:
                print('o',end="")
                
            elif x==0 and y!=f_x and y!=0:
                print('|',end="")
            elif y==0 and y!=f_x and x!=0:
                print('-',end="")
            elif y==0 and x==0 and f_x!=y:
                print('+',end="")
            else:
                print(" ",end="")
        print()
            
            
            
    
f()