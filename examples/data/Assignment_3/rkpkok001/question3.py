x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
l=len(x)
def topframe(z):
    for i in range(z):
        print("|"*(i)+"+"+"-"*(2*z+l-2*i)+"+"+"|"*(i))
        if i==z:
            break
def body(x):
    for i in range(y):
        print("|"*(z)+" "+x+" "+"|"*(z))

def bottomframe(z):
    for i in range(z):
        print("|"*(z-i-1)+"+"+"-"*(l+2*i+2)+"+"+"|"*(z-i-1))
        if 1>=z:
            break
topframe(z)
body(x)
bottomframe(z)