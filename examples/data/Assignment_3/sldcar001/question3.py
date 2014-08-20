def frame():
    mes=input("Enter the message:\n")
    n=len(mes)+2
    rep=eval(input("Enter the message repeat count:\n"))
    fr=eval(input("Enter the frame thickness:\n"))
    a=0
    repfr=fr
    b=n+2*fr
    while fr>0:
        b=n+2*fr-2
        print("|"*a,"+","-"*(b),"+","|"*a,sep='')
        fr-=1
        a+=1
    while rep>0:
        print("|"*repfr," ",mes," ","|"*repfr,sep='')
        rep-=1
    while repfr>0:
        repfr-=1
        print("|"*repfr,"+","-"*(b),"+","|"*repfr,sep='')
        fr+=1
        b=n+2*fr
        a-=1
frame()