msg=input("Enter the message:\n")
rpt=eval(input("Enter the message repeat count:\n"))
fthick=eval(input("Enter the frame thickness:\n"))
fc=fthick
fc2=1
mcount=rpt

for i in range(fthick*2+rpt):
    if fc>0:
        print((fthick-fc)*"|","+","-"*((len(msg)+2*fc)),"+",(fthick-fc)*"|",sep="")
        fc=fc-1
    elif mcount>0:
        print("|"*fthick,msg,"|"*fthick)
        mcount=mcount-1
    else:
        print((fthick-fc2)*"|","+","-"*((len(msg)+2*fc2)),"+",(fthick-fc2)*"|",sep="")
        fc2=fc2+1
        
        
    