#NDXKEE009
#Keegan Naidoo
#16 April 2014

import math   #makes use of functions from math library

fx = input("Enter a function f(x):\n")          #Input function
x=0
for x_cord in range(10,-11,-1):                 # Horizontal component    
    for y_cord in range(-10,11):                # Vertical Component
        
        x=y_cord
        new_fx=round(eval(fx))                  #Evaluate the function
        
        if new_fx== x_cord:                     #Populates the function onto the graph
            print("o",end="")
            
        if x_cord==0 and y_cord==0 and x_cord!= new_fx:      #Prints the origin of the graph if the function doesn't cut the origin
            print("+", end="")
        if x_cord ==0 and y_cord !=0 and x_cord!= new_fx:    #Prints the x-axis
            print("-",end="")
        if y_cord==0 and x_cord !=0 and x_cord !=new_fx:     #Prints the y-axis
            print("|",end="")
        if x_cord!= 0 and y_cord != 0 and x_cord!=new_fx:    #Prints the spaces between the x-axis and the outer most limit
            print(" ",end="")
            
    print()