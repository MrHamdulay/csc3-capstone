height = eval(input("Enter the height of the triangle:\n"))
space = height-1
i = 0
n = 1

while i < height:
    print(space*" ", n*"*", sep="")
    i+=1
    space-=1
    n+=2