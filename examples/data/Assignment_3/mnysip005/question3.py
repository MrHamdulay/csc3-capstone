x= input("Enter the message:\n")
y= eval(input("Enter the message repeat count:\n"))
z= eval(input("Enter the frame thickness:\n"))
a=0
for i in range(z,0,-1):
    b=len(x)+2*i
    print("|"*a,"+","-"*b,"+","|"*a,sep="")
    a+=1

for i in range(y):
    print("|"*z, x, "|"*z)

c = z-1
for i in range(z):
    d= len(x)+2*(i+1)
    print("|"*c,"+","-"*d,"+", "|"*c, sep="")
    c-=1