x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
a=len(x)+2
u=z
v=0
o=z
r=0
for i in range(z):
    print("|"*v,"+","-"*(2*u),"-"*2, "-"*(a-4),"+","|"*v,sep="")
    v=v+1
    u=u-1
for i in range(y):
    print("|"*z,x,"|"*z)

for i in range(o,0,-1):
    
    print("|"*(i-1),"+","-"*(a+r),"+","|"*(i-1),sep="")
    r=r+2