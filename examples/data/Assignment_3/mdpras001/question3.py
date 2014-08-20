x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))


a=0
b=len(x)+z*2
for i in range (z):
    print('|'*a,'+','-'*b,'+','|'*a,sep='')
    a+=1
    b-=2
for i in range(y):
    print('|'*z,x,'|'*z)
a-=1
b+=2
for i in range(z):
    print('|'*a,'+','-'*b,'+','|'*a,sep='')
    a-=1
    b+=2


