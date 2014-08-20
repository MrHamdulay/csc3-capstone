Msg=input("Enter the message:\n")
H=eval(input("Enter the message repeat count:\n"))
w=eval(input("Enter the frame thickness:\n"))
Bx=len(Msg)+2*w

if H==0 and w==0:
    print("")

for i in range(w):
    print("|"*i,"+","-"*(Bx-2*i),"+","|"*i,sep="")
for i in range(H):
    print("|"*w," ",Msg," ","|"*w,sep="")
for i in range(w-1,-1,-1):
    print("|"*(i),"+","-"*(Bx-2*i),"+","|"*(i),sep="")
    
