a=input("Enter the message: \n")
e=eval(input("Enter the message repeat count: \n"))
z=eval(input("Enter the frame thickness: \n"))
h=z-1
n=0
y=len(a)+2
x=len(a)+(2*z) #keep x outside loop otherwise it would keep resetting

for i in range (z):
    print("|"*n,"+",x*"-","+","|"*n,sep="")
    n=n+1
    x=x-2

for i in range (e):
    print(z*"|",a,z*"|")

for i in range (z):
    print("|"*h,"+",y*"-","+","|"*h,sep="")
    y=y+2
    h=h-1