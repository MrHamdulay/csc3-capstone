#Phumelele Ndimande
#Assignment 5

import math

def function():
    #input function
    f=input("Enter a function f(x):\n")
    #range and domain of graph
    for y in range(-10,11):
        for x in range(-10,11):
            if round(eval(f)) == -y: #graph plots
                print("o", end="")
            else:
                if (y==0) and (x==0):
                    print("+",end="")
                else:
                    if y==0: #x axis
                        print("-", end="")
                    else:
                        if x==0: #y axis
                            print("|", end="")
                        
                        else: #empty space where f is not defined
                            print(" ",end="")
        print()
                
function()

        
    
    