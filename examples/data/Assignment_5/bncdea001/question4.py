#Assignment 5, Question 4
#Graphing Functions
#Dean Bunce
#14 April 2014


import math
#Get an input from the user
fx=input("Enter a function f(x): \n")

#Create the 2D array      
for y in range(-10,11):
        for x in range(-10,11):
                #Flip the graph
                y_actual=-y
                
                #Make x equal to the function
                x_actual=eval(fx)
                x_actual=round(x_actual)
                
                #Printing out the graph of the function
                if y_actual==0 and x==0 and x_actual!=y_actual:
                        print("+", end="")
                elif y_actual==0 and x_actual!=y_actual:
                        print("-", end="")
                elif x==0 and x_actual!=y_actual:
                        print("|", end="")
                elif y_actual==x_actual:
                        print("o", end="")
                else: print(" ", end="")
        print()
        


    
    