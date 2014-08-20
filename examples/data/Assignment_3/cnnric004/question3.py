message = input("Enter the message:\n")
messager = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

for j in range(frame):
        print("|"*j,"+","-"*(len(message)+2+2*(frame-1)-j*2),"+","|"*j,sep="")

for i in range(messager):
        print("|"*frame,message,"|"*frame)
        
for k in range(frame,0,-1):
        print("|"*(k-1),"+","-"*(len(message)+4+2*(frame-1)-k*2),"+","|"*(k-1),sep="")