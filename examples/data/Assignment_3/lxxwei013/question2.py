def triangle():
    x=eval(input("Enter the height of the triangle:\n"))
    i=1
    gap=(x-1)
    while i<=x:
        print(" "*gap, end="")
        print("*"*(2*i-1))
        gap=gap-1
        i=i+1
triangle()        