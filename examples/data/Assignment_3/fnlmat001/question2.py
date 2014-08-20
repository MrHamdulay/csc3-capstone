# Matthew Finlayson - FNLMAT001
# 22/03/14
# Assignment 3 - Question 2

height = int(input("Enter the height of the triangle: \n"))
numSpace = height-1
for i in range(height):
    numStars = "*"*(2*i+1)
    print(" "*numSpace + numStars)
    numSpace-=1