#Program to locate palindromic primes
#Tinotenda Chemvura (CHMTIN004)
#24 March 2014

#_____________________Program starts here__________________________*

msg=input("Enter the message:\n")
msgRcount=eval(input("Enter the message repeat count:\n"))
frameThick=eval(input("Enter the frame thickness:\n"))

if frameThick >= 1:
    lenTB=(frameThick*2)+(len(msg))
    print("+","-"*lenTB,"+",sep="")
    cnt=lenTB-2
    for i in range(1,frameThick,1):
        if frameThick<=1: break
        else:
            print("|"*i,"+","-"*cnt,"+","|"*i,sep="")
            cnt=cnt-2
    for j in range(msgRcount):
        print("|"*frameThick,msg,"|"*frameThick)
    cnt2=len(msg)+2
    for i in range(frameThick-1,0,-1):
        if frameThick<=1: break
        else:
            print("|"*i,"+","-"*cnt2,"+","|"*i,sep="")
            cnt2=cnt2+2
            
    print("+","-"*lenTB,"+",sep="")