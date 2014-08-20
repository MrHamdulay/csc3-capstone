# program to draw a rectangle of a given height using the "*" character
# by: khadeejah omar
# 15 March 2014

height = eval(input("Enter the height of the rectangle: \n"))
width = eval(input("Enter the width of the rectangle: \n"))

for i in range(height) :
              print("*" * width)