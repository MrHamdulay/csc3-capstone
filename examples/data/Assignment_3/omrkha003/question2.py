# program to draw an inverted iscoceles of given height using the "*" character
# by: khadeejah omar
# 16 March 2014

height = eval(input("Enter the height of the triangle: \n"))
n = height - 1 # initial amount white spaces
length = 1 
height2 = length - 1 # right half of triangle
while n != -1 :
    space = " " * n
    print(space, "*" * length, sep="", end="") # prints left-half of triangle
    print(height2 * "*") # prints right-half of triangle
    height2 = height2 + 1
    length = length + 1
    n = n - 1 # new amount of white spaces