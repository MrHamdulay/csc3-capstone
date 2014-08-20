height = eval(input("Enter the height of the triangle:\n"))

for i in range(0,height):
    print(" "*((height)-i-1), "*"*((i*2)+1), sep="")