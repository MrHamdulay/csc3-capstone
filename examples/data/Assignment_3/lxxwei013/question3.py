def frame():
    x=input("Enter the message:\n")
    y=eval(input("Enter the message repeat count:\n"))
    z=eval(input("Enter the frame thickness:\n"))
    
    if z>0:
        print("+", "-"*(len(x)+2*z),"+", sep="")
    a=1
    b=1
    for i in range(z-1):
        print("|"*a,"+", "-"*(len(x)+2*z-2*b), "+", "|"*a, sep="")
        a+=1
        b+=1
    for j in range(y):
        print("|"*z, " ", x, " ", "|"*z, sep="")
    c=z-1
    d=z-1
    for k in range(z-1):
        print("|"*c, "+", "-"*(len(x)+2*z-2*d), "+", "|"*c, sep="")
        c-=1
        d-=1
    if z>0 and y>0:
        print("+", "-"*(len(x)+2*z),"+", sep="")
frame()
        
        
    