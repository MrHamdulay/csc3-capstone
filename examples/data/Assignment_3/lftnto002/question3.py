message= input("Enter the message:\n")
repeatcount= eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))
dashcount= len(message)+frame*2 #intialize dashcount
bordercount=frame #intialize border thickness
outsidechar1="+"
outsidechar2="+"

for i in range(frame):
    print(outsidechar1,"-"*dashcount,outsidechar2,sep="")
    dashcount=dashcount-2
    outsidechar1="|"+outsidechar1
    outsidechar2= outsidechar2+"|"
    
for j in range(repeatcount):
    print("|"*frame,message,"|"*frame)
x=1  
y=2
for k in range(frame):
    print(outsidechar1[x:],"-"*(dashcount+y),outsidechar2[0:len(outsidechar2)-x],sep="")
    x=x+1
    y=y+2
  

