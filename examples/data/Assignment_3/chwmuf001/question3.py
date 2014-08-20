mes=input("Enter the message:\n")
rep=eval(input("Enter the message repeat count:\n"))
f=eval(input("Enter the frame thickness:\n"))
l=len(mes)+(2*f)

#print("+", "-"*l,"+",sep="")

#l-=2
i=0

while i<f:
    print("|"*(i),"+", "-"*l,"+","|"*(i),sep="")
    l-=2
    i+=1

x=0

while x<rep:
    print("|"*f, mes,"|"*f)
    x+=1

i=f-1
l+=2

while i>=0:
    print("|"*(i),"+", "-"*l,"+","|"*(i),sep="")
    l+=2
    i-=1    
    
#l=len(mes)+(2*f)
#print("+", "-"*l,"+",sep="")
