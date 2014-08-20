# This program displays a triangle of height supplied by the user

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 19 March 2014

height = eval(input("Enter the height of the triangle:\n"))
space = height - 1
width = 1
for i in range(1,height+1):
    print(" "*space,end='')
    print("*"*width)
    width = width + 2
    space = space - 1

#Sample I/O:

#Enter the height of the triangle:
#5
#    *
#   ***
#  *****
# *******
#*********