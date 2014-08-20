#display message in frame
def display():
    x=input("Enter the message:\n")
    y=eval(input("Enter the message repeat count:\n"))
    z=eval(input("Enter the frame thickness:\n"))
    r=2
    e='|'
    g='+'
    h=len(x)+2
    k=h+2*z-2
    for f in range(0,z,):
        l=(k-2*f)
        print((e*f),g,('-'*l),g,(e*f),sep='')
    for t in range(0,y):
        print((e*z)+(' '+x+' ')+(e*z))
    for j in range(z-1,-1,-1):
        n=k-2*j
        print((e*j),g,('-'*n),g,(e*j),sep='')
display()