# Assignment 3 question 2
# Amy Brodie
# 27/03/2014

height = eval(input("Enter the height of the triangle:\n"))
length = 1
spaces = height - 1
for i in range(height):
    print(" "*spaces,"*"*length,sep="")
    length += 2
    spaces -= 1