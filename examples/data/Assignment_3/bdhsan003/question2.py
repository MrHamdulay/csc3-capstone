#STUDENT NUMBER:BDHSAN003


def triangle():
    triheight1=eval(input("Enter the height of the triangle:\n"))
    s=1
    shape=triheight1
    for i in range(0,triheight1):
        print(' '*(shape-1),end='')
        print('*'*(s))
        shape=shape-1
        s=s+2

triangle()