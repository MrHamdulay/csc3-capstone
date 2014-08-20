# This program displays a rectangle based on the width and height input

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 19 March 2014

height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))

for i in range(height):
    print("*"*width)

#Sample I/O:

#Enter the height of the rectangle:
#3
#Enter the width of the rectangle:
#7
#*******
#*******
#*******