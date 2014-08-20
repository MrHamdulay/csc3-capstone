#program to draw a text-based graph from mathematical function f(x)
#KNNSAD001

import math   #importing from math lirary in python 


#defining variables 
mathfunction = input("Enter a function f(x):\n")

#introducing y increament 
yaxis_increase = 4.9/10

for y in range(10,-11,-1):
        for x in range(-10,11):
        
                if (y-yaxis_increase) <= eval(mathfunction) <= (y+yaxis_increase):
                        print("o", end="")
            
            
                else:   
                        if x==0 and y==0:
                                print("+", end="")
            
                        elif y==0:
                                print("-", end="")
                
                        elif x==0:
                                print("|", end="")
                
                        else:
                                print(" ", end="")
                        
                        print()
        
        