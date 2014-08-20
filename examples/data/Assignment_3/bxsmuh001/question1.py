#Assignment 3, Question 1
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 26/03/2014

#This program is used to create a simple rectangle based on the user input of width and height.

#Defining the function rectangle() to create the pattern.
def rectangle():    
    #Pre-condition: Input Height and Width of Rectangle.
    #Post-condition: Output rectangle shape.    
    heightOfRectangle = eval(input("Enter the height of the rectangle:\n"))
    widthOfRectangle = eval(input("Enter the width of the rectangle:\n"))
    
    for i in range(heightOfRectangle):
            print("*" * widthOfRectangle)        

rectangle()