message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
message_length = len(message)

for i in range(0,frame):
    print("|"*i,"+",(2*(frame-i)+message_length)*"-","+","|"*i,sep="")
    
for j in range(0,repeat):
    print("|"*frame,message,"|"*frame)
k=2
for i in range(frame,0,-1):
    print("|"*(i-1),"+",(message_length+k)*"-","+","|"*(i-1),sep="")
    k+=2