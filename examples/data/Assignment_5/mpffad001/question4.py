#a program to draw a text-based graph of a mathematical function f(x). 
#fadzai mupfunya
#14 April 2014

import math

def graph():
    equation_string=input("Enter a function f(x):" '\n')
    for y in range(10,-11,-1):            #for the y values
        for x in range (-10,11):           #for the x values
            equation=round(eval(equation_string))
            if y==equation:
                print("o",end='')
            elif y==0 and x==0:             #for the origin
                print("+",end='')
            elif y==0:                    #for the x-axes
                print("-",end='')
            elif x==0:                    #for the y-axes
                print("|",end='')
            else:
                print(" ",end='')
        print()
        
graph()