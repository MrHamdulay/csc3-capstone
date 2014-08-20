height=eval(input("Enter the height of the triangle:\n"))
x = 1
while 0<height:
    print(" "*(height-1),"*"*x, sep="")
    height=height-1
    x=x+2