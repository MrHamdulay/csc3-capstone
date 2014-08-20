x=input("Enter the message:\n")
rpt=eval(input("Enter the message repeat count:\n"))
width=eval(input("Enter the frame thickness:\n"))
z=len(x)+2
y=rpt
w=2*(width-1)
f=width
e=0
for i in range(width):
    print("|"*(i),"+","-"*(z+w),"+","|"*(i),sep="")
    w=w-2
for i in range(rpt):  
    print("|"*width,x,"|"*width)
for i in range(f,0,-1):
    print("|"*(i-1),"+","-"*(z+e),"+","|"*(i-1),sep="")
    e=e+2