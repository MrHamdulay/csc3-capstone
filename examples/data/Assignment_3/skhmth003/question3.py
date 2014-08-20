x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
a=len(x)
c=a+1+1+(z-1)*(2)
d=0
for b in range(z):
        print("|"*d,"+","-"*c,"+","|"*(d),sep="")
        c-=2
        d+=1
for b in range(y):
        print("|"*z," ",x," ","|"*z,sep="")
c=1*a+1+1
d=z-1
for b in range(z):
        print("|"*d,"+","-"*c,"+","|"*(d),sep="")
        c+=2
        d-=1