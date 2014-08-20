""" A program to draw a text-based graph of a mathematical function f(x)
Author: Afika Nyati
Date: 16 April 2014 """


import math # Imports Math Library



def draw_graph():
    
    function = input("Enter a function f(x):\n") # Asks user for a graph
    
    for y in range (-10, 11):
        y_increment = 1/2  # Allows a range of y values to print, so that the graph can look full.
        
        for x in range (-10, 11):
            
            if (-y - y_increment) <= eval(function) <= (-y + y_increment) : # If the evaluated function is between a range of y-values, it prints 'o'.
                print("o", end = "")             
            
            elif x == 0 and y == 0: # If the point is the origin, it prints a '+'.
                print("+", end = "") 
             
            
            elif y == 0: # If the y-value is '0', it prints '-'.
                print("-", end ="")
                
            elif x == 0: # If the x-value is '0', it prints '|'.
                print ("|", end ="")
            
                
            else:
                print(" ", end = "") #If the co-ordinate pair does not corrspond with any decisions above, it prints a space.
        print() # Goes to the next line.
    
                
draw_graph()
            