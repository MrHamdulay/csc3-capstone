height=eval(input("Enter the height of the triangle:""\n"))
gap=height-1
for row in range(1,(height+1)):
    print(gap*" ", end="")
    width=2*row-1
    print(width*"*")
    gap=gap-1
    