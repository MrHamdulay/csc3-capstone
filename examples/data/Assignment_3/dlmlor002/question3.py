message=input("Enter the message:\n")
messageRepeatCount=eval(input("Enter the message repeat count:\n"))
frameThickness=eval(input("Enter the frame thickness:\n"))

k=(frameThickness+len(message)+frameThickness)
i=0
while -1<i<frameThickness:
    print("|"*i,"+","-"*k,"+","|"*i,sep="")
    i=i+1
    k=k-2
for i in range(messageRepeatCount):
    print("|"*frameThickness,message,"|"*frameThickness)
k=(len(message)+2)
i=frameThickness-1
while -1<i<frameThickness:
    print("|"*i,"+","-"*k,"+","|"*i,sep="")
    i=i-1
    k=k+2