mesg=input("Enter the message:\n")
mes=len(mesg)
rpt=eval(input("Enter the message repeat count:\n"))
thkns=eval(input("Enter the frame thickness:\n"))
th=thkns
k=0
for i in range(thkns*2+rpt):
    if(i in range(0,thkns)):
        print("|"*i,"+","-"*(2*th+mes),"+","|"*i,sep='')
        th-=1;
    elif(i in range(thkns+rpt, thkns*2+rpt)):
        print("|"*(thkns*2+rpt-i-1),"+","-"*(2*k+mes+2),"+","|"*(thkns*2+rpt-i-1),sep='')
        k+=1
        
    elif(i in range(thkns, thkns+rpt)):
         print("|"*thkns,mesg,"|"*thkns)