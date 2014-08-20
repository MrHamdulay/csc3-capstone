def makeframe():
    mess = input("Enter the message:\n")
    repcount = eval(input("Enter the message repeat count:\n"))
    framethick = eval(input("Enter the frame thickness:\n"))
    mess = " " + mess + " "
    for i in range(framethick,0,-1):
        if i == framethick:
            print("+","-"*(len(mess)+2*framethick-2),"+",sep='')
        else: print("|"*(framethick-i),"+","-"*(len(mess)+2*i-2),"+","|"*(framethick-i),sep='')
    for i in range(repcount):
        print("|"*framethick,mess,"|"*framethick,sep='')
    for i in range(1,framethick+1):
        if i == framethick:
            print("+","-"*(len(mess)+2*framethick-2),"+",sep='')
        else: print("|"*(framethick-i),"+","-"*(len(mess)+2*i-2),"+","|"*(framethick-i),sep='')
            
        
makeframe()

