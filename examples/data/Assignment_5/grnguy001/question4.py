#Given a function: Drawing it
#Guy Green
#Assignment 5
#Question 4

import math



#Asking user for the function
equation=input("Enter a function f(x):\n")

#Creating Grid
for y_axis in range (10,-11,-1):
    for x_axis in range (-10,11):
        
        #Plugging in x values
        x=x_axis
        
        #Making sure the values for the graph are integers so that it can actually plot the points
        integer_value=round(eval(equation))
        
        #Plotting values on graph
        if integer_value==y_axis:
            print("o", end="") #end='' is needed to that it doesn't skip a line each time
        
        #Plotting Origin        
        elif y_axis==0 and x_axis==0:
            print("+", end="")
        
        #Plotting  x-axis
        elif y_axis==0:
            print("-", end="")
        
        #Plotting y-axis
        elif x_axis==0:
            print("|", end="")
        
        #Printing empty spaces
        else:
            print(" ", end="")
    
    #Starting new line after each value in the y-axis
    print()