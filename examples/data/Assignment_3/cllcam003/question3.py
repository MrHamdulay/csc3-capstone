message=input("Enter the message:\n")
repeat= eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n")) 
length=len(message) 
a=0
b=1
for i in range(thickness, 0,-1):
    c=length+2*(i)
    print("|"* a,"+"*b,"-"*c,"+"*b,"|"* a,sep="")
    a=a+1
    b=b
for i in range(repeat):
    print("|"*thickness,message,"|"*thickness)
x=thickness-1
y=1
z=length+2
for i in range(thickness):
    print("|"* x,"+"*y,"-"*z,"+"*y,"|"* x,sep="")
    x=x-1
    y=y
    z+=2
 