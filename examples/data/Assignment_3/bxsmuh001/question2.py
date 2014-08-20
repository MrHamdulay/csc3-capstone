#Assignment 3, Question 2
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 27/03/2014

#This program is used to create a triangular shape based on the user input for the height of the triangle.

#Defining the function triangle() to create the pattern.
def triangle():
    #Pre-condition: Input height of the Triangle.
    #Post-condition: Generate triangular pattern.
    heightOfTriangle = eval(input("Enter the height of the triangle:\n"))
    spaceAlignment = heightOfTriangle - 1 #Initializing the spacing for the first row.
    starAlignment = 1 #Initializing the number of * for the first row == 1.
    
    #Pre-condition: Make first row with spacing equal to number of rows - 1, followed by 1 star and again folllowed by the same spacing.
    #Post-condition: Iterate through heightOfTriangle for each row, decreasing the spacing by subtracting 1 for each row and increasing the number of stars by adding 2 for each row.
    for i in range(heightOfTriangle):
        print((" " * spaceAlignment) + ("*" * starAlignment) + (" " * spaceAlignment))
        spaceAlignment -= 1 #Space should decrease by 1.
        starAlignment += 2 #Number of stars should increase by 2.

triangle()