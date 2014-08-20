"""PIET MOTALAOTA
17 APRIL 2014"""
import math

def f():
    
    function=input('Enter a function f(x):\n')
    for y in range(10,-11,-1):
        #y axis
    
        for x in range(-10,11):
            #x axis
            """compute f(x) and round the value to no decimal places"""
            f = round(eval(function))

            if y ==f:
                print('o',end="")
                

            elif x==0 and y!=f and y!=0:
                print('|',end="")

            elif y==0 and y!=f and x!=0:
                print('-',end="")

            elif y==0 and x==0 and f!=y:
                print('+',end="")

            else:
                print(" ",end="")
        print()
            
            
            
    
f()