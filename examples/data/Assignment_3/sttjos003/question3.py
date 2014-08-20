message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
x=len(message)
r=0
f=0

while f<frame:
    print("|"*f, "+", "-"*(x+(frame*2)-(f*2)), "+", "|"*f, sep="")
    f=f+1

while r<repeat:
    print("|"*f, message, "|"*f)
    r=r+1
    
f=f-1
while f>-1:
    print("|"*f, "+", "-"*(x+(frame*2)-(f*2)), "+", "|"*f, sep="")
    f=f-1
    