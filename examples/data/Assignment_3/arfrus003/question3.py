x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
a=0
b=len(x)+2*z
for i in range(z):
    print("|"*a,"+","-"*b, "+", "|"*a, sep="")
    a+=1
    b-=2
for u in range(y):
    print("|"*z, x, "|"*z) 
d=z-1
f=len(x)+2
for r in range (z):
    print("|"*d, "+", "-"*f, "+", "|"*d, sep="")
    d-=1
    f+=2