"""Draw text-based graph of math function
Ross Eyre
15/04/2014"""

import math   

def drawGraph():
    
    #get user input
    func = input("Enter a function f(x):\n")
    
    x = 0
    y = 0
    
    for rows in range(10,-11,-1):
        for col in range(-10,11,1):
            
            #make x = to current collumn
            x=col
            #evaluate as math function and round off
            R_func = round(eval(func))
            
       
            #print function
            if R_func == rows:
                print("o", end="")
                
            #print center
            if rows==0 and col==0 and not R_func==rows:
                print("+",end="")
            #print rows-arowsis
            if col==0 and not rows==0 and not rows == R_func:
                print("|", end="")            
            #print col-arowsis    
            if rows ==0 and not col==0 and not rows == R_func:
                print("-", end="")
            #if nothing in block, print a space
            else:
                if not rows==0:
                    if not col==0:
                        if not R_func==rows:
                            print(" ", end="")
            
        print()
            
            
    
                            
drawGraph() 