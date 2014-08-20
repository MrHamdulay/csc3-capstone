message=input("Enter the message:\n")count=eval(input("Enter the message repeat count:\n"))framethick=eval(input("Enter the frame thickness:\n"))length=len(message)

for i in range(0,framethick):
    print("|"*i,"+","-"*(length+2*(framethick-i)),"+","|"*i,sep="")       
for i in range(count):
    print("|"*framethick,message,"|"*framethick,end="\n")
for i in range(framethick-1,-1,-1):
        print("|"*i,"+","-"*(length+2*(framethick-i)),"+","|"*i,sep="")
