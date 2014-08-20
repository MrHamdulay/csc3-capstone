height = eval(input("Enter the height of the triangle:\n"))

space = height
star = 1

for i in range(0,height):
    print(" "*(space-1),"*"*star," "*(space-1),sep="")
    space = space - 1
    star = star + 2