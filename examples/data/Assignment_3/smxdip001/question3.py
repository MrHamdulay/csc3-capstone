#question3

x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
a=eval(input("Enter the frame thickness:\n"))
b=a-1
n=0
w=len(x)+2
z=len(x)+(2*a)

for i in range (a):
    print("|"*n,"+",z*"-","+","|"*n,sep="")
    n=n+1
    z=z-2

for i in range (y):
    print(a*"|",x,a*"|")
    
for i in range (a):
    print("|"*b,"+",w*"-","+","|"*b,sep="")
    w=w+2
    b=b-1