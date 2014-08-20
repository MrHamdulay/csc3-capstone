#Dumisani J Nyathi

def box():
    x=input("Enter the message:\n")
    y=eval(input("Enter the message repeat count:\n"))
    z=eval(input("Enter the frame thickness:\n"))
    j='|'
    n='+'
    h=len(x)+2
    k=h+2*z-2
    for v in range(0,z):
        l=(k-2*v)
        print((j*v),n,('-'*l),n,(j*v),sep='')
    for m in range(0,y):
        print((j*z)+(' '+x+' ')+(j*z))
    for c in range(z-1,-1,-1):
        f=k-2*c
        print((j*c),n,('-'*f),n,(j*c),sep='')
box()