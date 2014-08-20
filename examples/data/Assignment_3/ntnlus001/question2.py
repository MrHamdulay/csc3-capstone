height=eval(input("Enter the height of the triangle:\n"))
space=height-1
addition=1
for i in range(height):
    print(" "*space,"*"*addition, sep="")
    addition=addition+2
    space=space-1
    