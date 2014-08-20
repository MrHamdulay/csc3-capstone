x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
a="+"
b="|"
c="-"
for i in range(0,z):
    print(b*i, a, c*(len(x)-2*i+2*z), a, b*i, sep='')
for i in range(y):
    print(b*z, x, b*z)
for i in range(z-1, 0-1, -1):
    print(b*i, a, c*(len(x)-2*i+2*z), a, b*i, sep='')
    
       