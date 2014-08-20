x=input("Enter the message:""\n")
y=eval(input("Enter the message repeat count:""\n"))
z=eval(input("Enter the frame thickness:""\n"))
a=z
b=0
c=1
d=z-1
for i in range(z):
    print("|"*b,"+","-"*a,"-"*len(x),"-"*a,"+","|"*b,sep="")
    b+=1
    a-=1
for i in range(y):
    print("|"*z,x,"|"*z)
for i in range(z):
    print("|"*d,"+","-"*c,"-"*len(x),"-"*c,"+","|"*d,sep="")
    c+=1
    d-=1