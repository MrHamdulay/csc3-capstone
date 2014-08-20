def frame():
    a=input("Enter the message:\n")
    x=eval(input("Enter the message repeat count:\n"))
    y=eval(input("Enter the frame thickness:\n"))
    l=len(a)
    g=0
    f="|"
    h="-"
    w=l+2*y
    for i in range(y):
        print(g*f,"+",h*w,"+",g*f,sep="")
        g=g+1
        w=w-2
        k=g-1
        s=w+2
    for i in range(x):
        print(y*f,a,y*f)
    for i in range(y):
        print(k*f,"+",h*s,"+",k*f,sep="")
        k=k-1
        s=s+2
frame()
    