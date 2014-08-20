message=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
length=len(message)
p=thickness*2
length=length+p
for n in range(0,thickness):
    print("|"*n,"+","-"*(length),"+","|"*n,sep="")
    length-=2
for i in range (0,count):
    print("|"*thickness," ",message," ","|"*thickness,sep='')
t=length+2
for n in range(thickness-1,-1,-1):
    print("|"*n,"+","-"*t,"+","|"*n,sep="")
    t+=2