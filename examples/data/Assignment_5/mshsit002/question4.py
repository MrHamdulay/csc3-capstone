# a program to draw a text-based graph of a mathematical function f(x)
#Author: Sithembiso
#16 April 2014


import math

def graph():
    """ this is the function that will print out a text-based graph of 
    a mathematical function f(x)
    """
    
    # prompt the user for the equation of the graph
    graph = input("Enter a function f(x): \n")
    
    # a loop that will produce the graph
    for y in range(10,-11,-1):
        for x in range(-10,11):
            
            # if the rounded value of the graph is equal to the value of y,
            # axis
            if y == round(eval(graph)):
                print("o", end = "")
            
            #axis 
            elif x == 0 and y == 0:
                print("+", end = "")
            
            # if the graph is not valid or undefined  at some value of x, print a -
          
          
            elif x == 0:
                print("|", end = "")
            
            # if the graph is not valid or undefined  at some value of x, print a -
            elif y == 0:
                print("-", end = "")
    
            else:
                print(" ", end = "")
        print("")
        
graph()