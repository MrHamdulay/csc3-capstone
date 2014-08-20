h=eval(input('Enter the height of the triangle:\n'))
y=1
z=h-1
for i in range(h):
    print(z*" ",y*"*",sep="")
    y=y+2
    z=z-1