# 24 March 2014
# Jaren Hendricks
# Program to print a Isoceles triangle 

h = eval(input("Enter the height of the triangle:\n"))

icount = 0
counter = -1
while icount < h:
    icount+=1
    counter+=1
    stars = (counter + icount) * "*"
    spaces = (h-counter-1) * " "
    print (spaces + stars)