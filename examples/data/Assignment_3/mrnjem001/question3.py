msg=input("Enter the message:\n")
msg=" "+msg+" "
rep=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))

for i in range(1,frame+1):
    print((i-1)*"|","+","-"*(len(msg)+2*(frame-1)-2*(i-1)),"+",(i-1)*"|",sep="")
for j in range(1,rep+1):
    print("|"*frame,msg,"|"*frame,sep="")
for k in range(frame,0,-1):
    print((k-1)*"|","+","-"*(len(msg)+2*(frame-1)-2*(k-1)),"+",(k-1)*"|",sep="")