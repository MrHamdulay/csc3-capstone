def poster():
    m=input("Enter the message:\n")
    c=eval(input("Enter the message repeat count:\n"))
    f=eval(input("Enter the frame thickness:\n"))
    d=len(m)+(2*f)
    
    for i in range(f):
        print("|"*i,"+","-"*d,"+","|"*i,sep="",end="\n")
        d=d-2
        
    for i in range(c):
        print("|"*f,m,"|"*f)
        
    for i in range(f-1,-1,-1):   
        print("|"*i,"+","-"*(d+2),"+","|"*i,sep="",end="\n")    
        d=d+2
        
poster()