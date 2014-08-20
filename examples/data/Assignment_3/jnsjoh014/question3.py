def frame():
    mesg = input("Enter the message:\n")
    rept = eval(input("Enter the message repeat count:\n"))
    frameTh = eval(input("Enter the frame thickness:\n"))
    
   
    numDashes = (len(mesg)+(2*frameTh))
    #frameTh loop
    for i in range(frameTh):
       
        print(("|"*i),"+","-"*numDashes,"+",("|"*i),sep="",end="\n")
        
        if (i+1)==frameTh:
            for j in range(rept):
                print(("|"*i),"| ",mesg," |",("|"*i),sep="",end="\n")
        numDashes = numDashes-2   
    for k in range(frameTh):        
        print(("|"*(frameTh-k-1)),"+","-"*(numDashes+2*k+2),"+",("|"*(frameTh-k-1)),sep="",end="\n")
   
frame()    