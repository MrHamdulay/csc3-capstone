#Kalind Ramnarayan

x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))

a=len(x)+2*z
for i in range(z):
    print("|"*i,"+","-"*a,"+","|"*i,sep="")
    a=a-2
    
for i in range(y):
    print("|"*z," ",x," ","|"*z,sep="")

a=len(x)+2
for i in range(z-1,-1,-1):
    print("|"*i,"+",a*"-","+","|"*i,sep="")
    a=a+2