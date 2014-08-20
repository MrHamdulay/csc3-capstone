# question1.py
# program to draw a rectangle of a given height and width using the "*" character
# author: bxtnaa002

height = eval(input("Enter the height of the rectangle:\n"))      
width = eval(input("Enter the width of the rectangle:\n"))
for i in range(height):
   print("*"*width)