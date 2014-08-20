message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
x=0
y=1
z=0
while x<frame:
    print("|"*x,"+","-"*(len(message)+(2*frame)-(2*x)),"+","|"*x,sep="")
    x=x+1
while y<=repeat:
    print("|"*frame,message,"|"*frame)
    y=y+1
while frame>0:
    print("|"*(frame-1),"+","-"*(len(message)+2+z),"+","|"*(frame-1), sep="")
    frame=frame-1
    z=z+2