#ASSIGNMENT_4
#QUESTION_3
#ASIL_MOTALA
#MTLASI002
x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
m=len(x)
for i in range(z,0,-1):
    print("|"*(z-i),"+","-"*(m+2*i),"+","|"*(z-i),sep="")
for j in range(y):
    print("|"*z,x,"|"*z)
for k in range(1,z+1,1):
    print("|"*(z-k),"+","-"*(m+2*k),"+","|"*(z-k),sep="")