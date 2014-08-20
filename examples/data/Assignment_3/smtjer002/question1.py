# A program to draw a rectangle with the size based on set of inputs
# Author: Jeremy Smith
# Student Number: SMTJER002

height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))

for i in range(height):
    print('*'*width)