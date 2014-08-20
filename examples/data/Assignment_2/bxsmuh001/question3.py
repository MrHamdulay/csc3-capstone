#Assignment 2, Question 3
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 09/03/2014

#The program is designed to find the area of a circle. However, a tricky part of
#this program is to calculate PI by implementing Vieta's Formula of PI in Python.

#Pre-condition: 
#1. Create function pi() to calculate PI by implementing Vieta's formula.
#2. Create a functoin area() which will use pi() and determine the area of a 
#circle from input of radius.
#Post-condition: Output vaule of Area of circle.

import math #Importing math library to use sqrt().    

#Defining the function area().
#Pre-condition: Output Approximation of PI, and get input of radius from user.
#Post-condition: Output Area of circle.
def area():
    #Calculating the value of PI.
    #Pre-condition: Implement Vieta's formula of PI and calculate PI.
    #Post-condition: Assign PI to the calculated value to 3 decimal places.    
    #Defining variables.
    numerator = 2
    denominator = math.sqrt(2)
    initialPi = (2 * (numerator/denominator)) #Initial Value of PI.
    pi = initialPi #Assigning PI to its initial value.
    nextTerm = 0 #Initializing the next term in the series as 0.
    
    #Executing the series, looping till nextTerm == 1 and finding PI accordingly.
    while(nextTerm != 1):        
        #The denominator keeps updating from its previous value.
        denominator = (math.sqrt(2 + denominator))
        nextTerm = (2/denominator) #nextTerm keeps updating till == 1.
        pi = (pi * nextTerm) #PI gets updated with the new value of nextTerm.
    
    #pi = round(pi,3) #Finally, PI is rounded to 3d.p, after the while loop ends.    
     
    print("Approximation of pi:", round(pi,3)) #Output value of PI
    
    #Defining user input for the value of the radius.
    radius = eval(input("Enter the radius:\n"))
    
    #Variable to calculate the area of the circle, rounded to 3 decimal places.
    area = round((pi * radius * radius), 3)
    
    #Output the area of the circle.
    print("Area:",area)
    
#Calling the function area().
area()