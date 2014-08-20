#Question 3
#By: Dean de Haast

msg=input("Enter the message:\n")
repeatcount=eval(input("Enter the message repeat count:\n"))
framethick=eval(input("Enter the frame thickness:\n"))



for i in range(framethick):
    print("|"*i,"+", "-"*(len(msg)+2+2*(framethick-1)-(i*2)),"+","|"*i,sep="")
    
for i in range(repeatcount):
    print("|"*(framethick),msg,"|"*framethick)
    
for i in range(framethick,0,-1):
    print("|"*(i-1),"+","-"*(len(msg)+4+2*(framethick-1)-(i*2)),"+","|"*(i-1),sep="")