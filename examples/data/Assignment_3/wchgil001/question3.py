p=input("Enter the message:""\n")
q=eval(input("Enter the message repeat count:""\n"))
r=eval(input("Enter the frame thickness:""\n"))
a=r
b=0
c=1
d=r-1
for i in range(r):
    print("|"*b,"+","-"*a,"-"*len(p),"-"*a,"+","|"*b,sep="")
    b+=1
    a-=1
for i in range(q):
    print("|"*r,p,"|"*r)
for i in range(r):
    print("|"*d,"+","-"*c,"-"*len(p),"-"*c,"+","|"*d,sep="")
    c+=1
    d-=1