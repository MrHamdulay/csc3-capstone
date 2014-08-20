# A progam to draw an isoceles triangle whose size is based on an input
# Author: Jeremy Smith
# Student Number: SMTJER002

height=eval(input("Enter the height of the triangle:\n"))

spaces = height - 1

for i in range(height):
    print(" " * spaces, end="")
    print("*"*((i+1)*2-1))
    spaces-=1
