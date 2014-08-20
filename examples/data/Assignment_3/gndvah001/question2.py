x=eval(input("Enter the height of the triangle:\n"))
y=1
z=x-1
for i in range(x):
    print(z*" ",y*"*",sep="")
    y=y+2
    z=z-1