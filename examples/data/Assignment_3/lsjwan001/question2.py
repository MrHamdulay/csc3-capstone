def triangle():
    h=eval(input("Enter the height of the triangle:\n"))
    g=(2*h)//2
    for i in range(0,2*h,2):
        g=g-1
        print(' '*g,end='')
        print("*"*(i+1))

triangle()