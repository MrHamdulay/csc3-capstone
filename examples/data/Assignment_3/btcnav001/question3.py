def frame():
    x = input("Enter the message:\n")
    y = eval(input("Enter the message repeat count:\n"))
    z = eval(input("Enter the frame thickness:\n"))
    a=len(x)+2*z+2
    b=z-1
    
    for i in range(0,z):
        a=a-2
        print("|"*(i)+"+"+"-"*a+"+"+"|"*(i))
    for repeat in range(y):
        print("|"*z,x,"|"*z)
    
    for bottom in range(z-1,-1,-1):
        print("|"*b+"+"+"-"*a+"+"+"|"*b)
        b=b-1
        a=a+2
    
frame()