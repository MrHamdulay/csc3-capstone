#Program to draw a text based graph of a mathematical function
#Tsanwani Vhonani
#16 April 2014

import math
def graph():
    function=input('Enter a function f(x):\n')
    x=0
    y=0
    
    for row in range(10,-11,-1):
        for column in range(-10,11,1):
            x=column
            estimate=round(eval(function))
            if estimate==row:
                print("o", end='')
            
            if row==0 and column==0 and row!=estimate:
                print('+', end='')
            
            if column==0 and row!=0 and row!=estimate:
                print('|', end='')
                
            if row==0 and column!=0 and row!=estimate:
                print('-', end='')
            
            else:
                if row!=0:
                    if column!=0:
                        if row!=estimate:
                            print(' ', end='')
                            
        print()
            
graph()
    
    
    