height=eval(input("Enter the height of the triangle:\n"))
length=1
gap=height-1
for i in range(height):
    while length<=((height*2)-1):
        print(" "*gap,"*"*length,sep="")
        length+=2
        gap-=1
    print()