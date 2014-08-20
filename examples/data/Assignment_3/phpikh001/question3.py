M=input("Enter the message:\n")
R=eval(input("Enter the message repeat count:\n"))
F=eval(input("Enter the frame thickness:\n"))
if R==0 and F==0:
    print("")
else:
    p=len(M)+2*F
    print("+","-"*p,"+",sep="")
    for i in range(F-1):
        p=p-2
        print("|"*(i+1),"+","-"*p,"+","|"*(i+1),sep="")
    for i in range(R):
        print("|"*F,M,"|"*F)
    q=len(M)+2
    for i in range(F, 1,-1):
        print("|"*(i-1),"+","-"*q,"+","|"*(i-1),sep="")
        q=q+2
    p=len(M)+2*F
    print("+","-"*p,"+",sep="")