x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
b=eval(input("Enter the frame thickness:\n"))
v=b-1
u=len(x)
p=u+2
c=p+2*v
e=0
space=0
for i in range(v):
    print("|"*e,"+","-"*c,"+","|"*e,sep="")
    c=c-2
    space=space+1
    e=e+1
if b>0:
    print("|"*v,"+",p*"-","+","|"*v,sep="")
t=1
for i in range(0):
    print("|")
for i in range(y):
    print("|"*v,"|"*t, " ",x, " ","|"*v,end="|",sep="")
    print()
if b>0:
    print("|"*v,"+",p*"-","+","|"*v,sep="")
    
c=p+1
space=v-1
for i in range(v):
    print("|"*space,"+","-","-"*c,"+","|"*space,sep="")
    c=c+2
    space=space-1