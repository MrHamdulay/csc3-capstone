height = eval(input("Enter the height of the triangle:\n"))
j = 1
space = height-1
for i in range(0,height,1):
    print(" "*space,"*"*j,sep = "")
    j +=2
    space -= 1