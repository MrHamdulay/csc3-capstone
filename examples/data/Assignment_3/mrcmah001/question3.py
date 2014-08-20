def frame():
    M=input("Enter the message:"'\n')
    N=eval(input("Enter the message repeat count:"'\n'))
    F=eval(input("Enter the frame thickness:"'\n'))
    p=len(M)+2*F
    for i in range(F):
        print("|"*i,"+","-"*p,"+","|"*i,sep="")
        p=p-2
    for i in range(N):
        print("|"*F,M,"|"*F)
    p=len(M)+2
    for i in range(F,0,-1):
        print("|"*(i-1),"+","-"*p,"+","|"*(i-1),sep="")
        p=p+2
        
    
frame()

