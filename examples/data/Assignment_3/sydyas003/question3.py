message=input("Enter the message:\n")
mes=len(message)
repeat=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
t=thickness
j=0
for i in range(thickness*2+repeat):
    if(i in range(0,thickness)):
        print("|"*i,"+","-"*(2*t+mes),"+","|"*i,sep='')
        t-=1;
    elif(i in range(thickness+repeat, thickness*2+repeat)):
        print("|"*(thickness*2+repeat-i-1),"+","-"*(2*j+mes+2),"+","|"*(thickness*2+repeat-i-1),sep='')
        j+=1
        
    elif(i in range(thickness, thickness+repeat)):
         print("|"*thickness,message,"|"*thickness)