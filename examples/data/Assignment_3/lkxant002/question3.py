msg=input("Enter the message:\n")
rep=eval(input("Enter the message repeat count:\n"))
frm=eval(input("Enter the frame thickness:\n"))

if frm!=0:         
    print("+","-"*(len(msg)+2*frm),"+",sep="")

for i in range(frm-1):
    print((i+1)*"|","+","-"*(len(msg)+(2*(frm-i-1))),"+",(i+1)*"|",sep="")
    
for i in range(rep):
    print(frm*"|",msg,frm*"|")

for i in range(frm-1):
    print((frm-(i+1))*"|","+","-"*(len(msg)+(2*(i+1))),"+",(frm-(i+1))*"|",sep="")
   
if frm!=0:         
    print("+","-"*(len(msg)+2*frm),"+",sep="")

