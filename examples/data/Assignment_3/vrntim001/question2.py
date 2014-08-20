height = eval(input("Enter the height of the triangle:\n"))
i = 0
x = (height-1)
width = 1
while i < height:
    print(" "*x,"*"*(width), sep="")
    i+=1
    x-=1
    width+=2
              