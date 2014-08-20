message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
len1=len(message)

for i in range(0,frame):
    print("|"*i,"+","-"*(len1+2*(frame-i)),"+","|"*i,sep="")
for i in range(repeat):
    print("|"*frame,message,"|"*frame,end="\n")
for i in range(frame-1,-1,-1):
    print("|"*i,"+","-"*(len1+2*(frame-i)),"+","|"*i,sep="")
    
