message=input("Enter the message:\n")

for i in range(0,framethick):
    print("|"*i,"+","-"*(length+2*(framethick-i)),"+","|"*i,sep="")       
for i in range(count):
    print("|"*framethick,message,"|"*framethick,end="\n")
for i in range(framethick-1,-1,-1):
        print("|"*i,"+","-"*(length+2*(framethick-i)),"+","|"*i,sep="")