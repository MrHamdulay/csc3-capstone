m=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))
e=len(m)+2*t
for i in range(0,t):
    print("|"*i,"+","-"*e,"+","|"*i,sep="")
    e-=2
for j in range(0,r):
    print("|"*t,m,"|"*t)
for k in range(t,0,-1):
    print("|"*(k-1),"+","-"*(e+2),"+","|"*(k-1),sep="")
    e+=2