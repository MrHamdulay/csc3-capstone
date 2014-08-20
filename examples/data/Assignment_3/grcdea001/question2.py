# Dean Gracey, GRCDEA001, Assignment 3, question 2

height = eval(input("Enter the height of the triangle:\n"))
stars = 1
space = height-1
for i in range(0,height,1):
    print(" "*space,end="")
    print("*"*stars,end="")
    print(" "*space)
    stars = stars+2
    space = space-1

    