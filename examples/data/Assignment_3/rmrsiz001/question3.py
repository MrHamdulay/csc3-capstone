b=input("Enter the message:\n")
v=eval(input("Enter the message repeat count:\n"))
q=eval(input("Enter the frame thickness:\n"))
r=q-1
z=len(b)
p=z+2
c=p+2*r
e=0
space=0
for i in range(r):
    print("|"*e,"+","-"*c,"+","|"*e, sep="")
    c=c-2
    space=space+1
    e=e+1
if q>0:
    print("|"*r,"+",p*"-","+","|"*r,sep="")
t=1
for i in range(0):
    print("|")
for i in range(v):
    print("|"*r,"|"*t, " ",b, " ","|"*r,end="|",sep="")
    print()
if q>0:
    print("|"*r,"+",p*"-","+","|"*r,sep="")
   
c=p+1
space=r-1
for i in range(r):
    print("|"*space,"+","-","-"*c,"+","|"*space,sep="")
    c=c+2
    space=space-1

        