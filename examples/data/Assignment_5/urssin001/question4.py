'''Write a program to draw a text-based graph of a mathematical function f(x)
Sinead Urisohn
15 April 2014'''

#import math library
import math
#get input from user
gra=input("Enter a function f(x):\n")
def graph():
    f=0
    #nested loops to scan through area of graph
    for y in range(-10,11): 
        
        for x in range(-10,11): 
            #round function f
            f=round(eval(gra)) 
            #change y to negative to mimic actual graph
            y_real=y*-1
            #if function is equal to y value print o
            if f==y_real:
                print("o",end="")
            #else print characters for axes or space
            elif x==0 and y==0:
                print("+",end="")
            elif x==0:
                print('|',end="")
            elif y_real==0:
                print('-',end="")
            else:
                print(" ",end="")
        #get new line
        print()
#invoke function
graph()
         