x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
l=len(x)+2
b=z-1
c=0
d=len(x)+z
e=z
for i in range(z):
    print("|"*c,"+", "-"*(d),z*"-", "+", "|"*c, sep='')
    c+=1
    d-=1
    z-=1
for i in range(y):
    print("|"*e, x, "|"*e)
for i in range(e):
    print("|"*b,"+", "-"*(l), "+", "|"*b, sep='')
    b-=1
    l+=2