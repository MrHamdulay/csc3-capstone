message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
m=0
while m<frame:
    print("|"*m,"+","-"*(len(message)+frame*2-m*2),"+","|"*m,sep="")
    m+=1
for i in range(repeat):
    print("|"*frame,message,"|"*frame)
m=0
l=len(message)+2
while frame>m:
    t=frame-m-1
    print("|"*t,'+',"-"*(l+m*2),"+","|"*t,sep="")
    m+=1

        