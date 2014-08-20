x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
b=2*z+len(x)
a=0
for i in range(z):
    print("|"*a+"+"*1+"-"*b+"+"*1+"|"*a)
    a=a+1
    b=b-2

for i in range(y):
    print("|"*z, x, "|"*z)
 
c=z-1
d=2+len(x)
for i in range(z):
    print("|"*c+"+"*1+"-"*d+"+"*1+"|"*c)
    c=c-1
    d=d+2
    
    
    