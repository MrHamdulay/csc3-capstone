msg=input("Enter the message:\n")
l=len(msg)

mrc=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
t=thickness
j=0
for i in range(thickness*2+mrc):
    if(i in range(0,thickness)):
        print("|"*i,"+","-"*(2*t+l),"+","|"*i,sep='')
        t-=1;
    elif(i in range(thickness+mrc, thickness*2+mrc)):
        print("|"*(thickness*2+mrc-i-1),"+","-"*(2*j+l+2),"+","|"*(thickness*2+mrc-i-1),sep='')
        j+=1
        
    elif(i in range(thickness, thickness+mrc)):
        print("|"*thickness,msg,"|"*thickness)