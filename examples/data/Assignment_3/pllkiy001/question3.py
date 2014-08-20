
M=input("Enter the message:""\n")
rc=eval(input("Enter the message repeat count: \n"))
thick=eval(input("Enter the frame thickness: \n"))
for i in range(thick):
    print("|"*(i),"+","-"*(len(M)+(2*thick)-(2*i)),"+","|"*(i),sep="")
for j in range(rc):
    print("|"*thick,M,"|"*thick)
for k in reversed(range(thick)):
    print("|"*(k),"+","-"*(len(M)+(2*thick)-(2*k)),"+","|"*(k),sep="")
