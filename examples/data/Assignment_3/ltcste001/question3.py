message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
n=(len(message)+2*(frame))
k=0
for i in range(frame):
    print("|"*k,"+",n*"-","+","|"*k,sep="")
    n=n-2
    k=k+1
for i in range(repeat):
    print("|"*frame, message, "|"*frame)
n=(len(message)+2)
k=frame-1
for i in range(frame,0,-1):
    print("|"*k,"+",n*"-","+","|"*k,sep="")
    n=n+2
    k=k-1
