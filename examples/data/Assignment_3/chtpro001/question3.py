msg=input("Enter the message:\n")
rep=eval(input("Enter the message repeat count:\n"))
thcknss=eval(input("Enter the frame thickness:\n"))
j=thcknss
for i in range(0,j,1) :
        print("|"*i,"+","-"*(len(msg)+2+2*(thcknss-1)-2*i),"+","|"*i,sep="")

i=1
while i<=rep:
        print("|"*thcknss," ",msg," ","|"*thcknss,sep="")
        i+=1
j=thcknss-1
for i in range(j,-1,-1):
        print("|"*i,"+","-"*(len(msg)+2+2*(thcknss-1)-2*i),"+","|"*i,sep="")        
        