'''Q4 of Assignment 5: Program to draw text-based graph of f(x)
Patrick Boroughs
16 April 2014'''

import math

function=input("Enter a function f(x):\n")

for y in range(10,-11,-1):
        for x in range(-10,11):
                if (y==round(eval(function))):
                        print("o",end="")                        
                elif (x==0 and y==0):
                        print("+",end="")
                elif (x==0):
                        print("|",end="")
                elif (y==0):
                        print("-",end="")
                else:
                        print(" ",end="")
        print()        

        
        
        '''
        yinc=2.5/30
        
        for y in range (-15,16):
                for x in range(0,62):
                        x_real = x/62 * math.pi*2
                        y_real = -y/15
                
                if (x_real==0 and y_real==0):
                        print("+",end="")
                elif (x_real==0):
                        print("|",end="")
                elif (y_real==0):
                        print("-",end="")
                elif y_real-yinc <= sin(x_real) <= y_real+yinc:
                        print("x",end="")
                else:
                        print(".", end="")
                
                print()
            
print("y=sin(x):\n")        
sin_graph()
        
    '''