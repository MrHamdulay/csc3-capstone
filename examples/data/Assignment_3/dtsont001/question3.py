def main3():
    msg = input("Enter the message:\n")
    rep = eval(input("Enter the message repeat count:\n"))
    thc = eval(input("Enter the frame thickness:\n"))
    x = thc-1
    y = 0
    frm1 = len(msg) +(thc*2)   
    frm2 = len(msg)+2
    for b in range(thc):
        print("|"*y,"+","-"*frm1,"+","|"*y,end="\n",sep="")
        y+=1
        frm1-=2
    for i in range(rep):
        print("|"*thc,msg,"|"*thc)
    for b in range(thc):
        print("|"*x,"+","-"*frm2,"+","|"*x,end="\n",sep="")
        x-=1
        frm2 +=2
main3()        
        