message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
a=0
b=1
length=len(message)
for i in range(thickness, 0, -1):
    c=length+2*i
    print("|"*a,"+","-"*c,"+","|"*a, sep="")
    a=a+1
for i in range(repeat):
    print(thickness*"|", message, thickness*"|")
x=thickness - 1
z=length+2
for i in range(thickness):
    print("|"*x,"+","-"*z,"+","|"*x, sep="")
    x=x-1
    z=z+2