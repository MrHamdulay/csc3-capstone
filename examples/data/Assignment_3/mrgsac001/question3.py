s=input("Enter the message: \n")
a=eval(input("Enter the message repeat count: \n"))
m=eval(input("Enter the frame thickness: \n"))
c=m-1
p=0
y=len(s)+2
x=len(s)+(2*m) 

for i in range (m):
    print("|"*p,"+",x*"-","+","|"*p,sep="")
    p=p+1
    x=x-2

for i in range (a):
    print(m*"|",s,m*"|")

for i in range (m):
    print("|"*c,"+",y*"-","+","|"*c,sep="")
    y=y+2
    c=c-1