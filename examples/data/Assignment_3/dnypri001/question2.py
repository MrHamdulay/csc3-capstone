def triangle():
    h=eval(input("Enter the height of the triangle:\n"))
    w=1
    gap=h-1
    for i in range(0,h):
        print(" "*gap,end="")
        print("*"*w)
        gap-=1
        w=w+2
triangle()
    