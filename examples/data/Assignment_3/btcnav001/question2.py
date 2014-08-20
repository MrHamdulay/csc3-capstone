def triangle():
    x=eval(input("Enter the height of the triangle:\n"))
    y=1
    for i in range(x-1,-1,-1):
        print(i*" ",y*"*",sep="")
        y=y+2
triangle()
