#Question 3
message=input("Enter the message:\n")
reapcount=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
lent=len(message)+2*thickness

for i in range(thickness):
    print("|"*i,"+","-"*(lent),"+","|"*i,sep="")
    lent-=2
for i in range(reapcount):
    print("|"*thickness, message, "|"*thickness)
for i in range(thickness-1,-1,-1):
    print("|"*i,"+","-"*(lent+2),"+","|"*i,sep="")
    lent+=2
    



