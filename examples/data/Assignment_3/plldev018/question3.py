a=input("Enter the message:\n")
b=eval(input("Enter the message repeat count:\n"))
c=eval(input("Enter the frame thickness:\n"))
d=len(a) + 2
x=len(a)
e=0
g=c
f=1
for i in range (c):
    print("|"*e,"+"*f,"-"*(d+(2*c-2)),"+"*f,"|"*e,sep="")
    e=e+1
    d=d-2
for i in range(b):
    print("|"*c,a,"|"*c)
for i in range (c):
    print("|"*(g-1),"+","-"*(d+(2*c-2)+2),"+","|"*(g-1),sep="")
    g=g-1
    d=d+2