message=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))

x=len(message)
y=0
q=frame-1
z=frame
w=1
while frame>0:
    print("|"*y, "+","-"*(x+2*frame),"+","|"*y, sep="")
    y=y+1
    frame=frame-1
while count>0:
    print("|"*z, message, "|"*z)
    count=count-1
while q>=0:
    print("|"*q, "+","-"*(x+2*w),"+","|"*q, sep="")
    q=q-1
    w=w+1        