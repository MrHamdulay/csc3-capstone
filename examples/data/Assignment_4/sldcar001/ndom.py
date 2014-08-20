def ndom_to_decimal(num):
    num=str(num)
    if len(num)==3:
        n1=int(num[-3])
        n2=int(num[-2])
        n3=int(num[-1])
    elif len(num)==2:
        n1=0
        n2=int(num[-2])
        n3=int(num[-1])
    elif len(num)==1:
        n1=0
        n2=0
        n3=int(num)        

    
    #so...
    dec=(((n1*6)+n2))*6+n3
    return dec
def decimal_to_ndom(num):
   # num=str(num)
    k=36
    y=6
    s=1
    d=1
    if num>=216:
        d=216
    elif num>=36:
        d=36
        k=y
        y=s
        s=0
    elif num>=6:
        d=6
        k=s
        y,s=0,0
    elif num>=1:
        d=1
        k,s,y=0,0,0
    a=num//d
    A=num%d
    if k>0:
        b=A//k
        B=A%k
        if y>0:
            c=B//y
            C=B%y
            if s>0:
                p=C//s
                P=C%s
                return(int(str(a)+str(b)+str(c)+str(p)))
            return(int(str(a)+str(b)+str(c)))
        return(int(str(a)+str(b)))
    return((int(str(a))))

def ndom_add (num1, num2):
    Num1, Num2=str(num1),str(num2)
    if len(Num1)==3:
        n1=int(Num1[-3])
        n2=int(Num1[-2])
        n3=int(Num1[-1])
    elif len(Num1)==2:
        n1=0
        n2=int(Num1[-2])
        n3=int(Num1[-1])
    elif len(Num1)==1:
        n1=0
        n2=0
        n3=int(Num1)
    if len(Num2)==3:
        n21=int(Num2[-3])
        n22=int(Num2[-2])
        n23=int(Num2[-1])
    elif len(Num2)==2:
        n21=0
        n22=int(Num2[-2])
        n23=int(Num2[-1])
    elif len(Num2)==1:
        n21=0
        n22=0
        n23=int(Num2)
    Nd1=decimal_to_ndom((n3+n23))    
    Nd2=decimal_to_ndom((n2+n22))
    if Nd1>=10:
        Nd2=Nd2+1
        Nd1=int(str(Nd1)[-1])
    Nd3=decimal_to_ndom((n1+n21))
    if Nd2>=10:
        Nd3=Nd3+1
        Nd2=int(str(Nd2)[-1])  
    NDA=int(str(Nd3)+str(Nd2)+str(Nd1))
    return(NDA)
    
def ndom_multiply(num1, num2):
    Num1, Num2=str(num1),str(num2)
    if len(Num1)==3:
        n1=int(Num1[-3])
        n2=int(Num1[-2])
        n3=int(Num1[-1])
    elif len(Num1)==2:
        n1=0
        n2=int(Num1[-2])
        n3=int(Num1[-1])
    elif len(Num1)==1:
        n1=0
        n2=0
        n3=int(Num1)
    if len(Num2)==3:
        n21=int(Num2[-3])
        n22=int(Num2[-2])
        n23=int(Num2[-1])
    elif len(Num2)==2:
        n21=0
        n22=int(Num2[-2])
        n23=int(Num2[-1])
    elif len(Num2)==1:
        n21=0
        n22=0
        n23=int(Num2)
    def ND1():
        Ndm1=n3*n23
        Ndm2=n2*n23
        if Ndm1>=10:
            Ndm1=int(str(Ndm1)[-1]) 
            Ndm2=Ndm2+int(str(Ndm1)[0])
        Ndm3=n1*n23
        if Ndm2>=10:
            Ndm2=int(str(Ndm2)[-1]) 
            Ndm3=Ndm3+int(str(Ndm2)[0])
        NDM1=int(str(Ndm3)+str(Ndm2)+str(Ndm1))
        return(NDM1)
    def ND2():
        Ndm1=n3*n22
        Ndm2=n2*n22
        if Ndm1>=10:
            Ndm1=int(str(Ndm1)[-1]) 
            Ndm2=Ndm2+int(str(Ndm1)[0])
        Ndm3=n1*n22
        if Ndm2>=10:
            Ndm2=int(str(Ndm2)[-1]) 
            Ndm3=Ndm3+int(str(Ndm2)[0])
        NDM2=int(str(Ndm3)+str(Ndm2)+str(Ndm1)+"0")   
        return(NDM2)
    def ND3():
        Ndm1=n3*n21
        Ndm2=n2*n21
        if Ndm1>=10:
            Ndm1=int(str(Ndm1)[-1]) 
            Ndm2=Ndm2+int(str(Ndm1)[0])
        Ndm3=n1*n23
        if Ndm2>=10:
            Ndm2=int(str(Ndm2)[-1]) 
            Ndm3=Ndm3+int(str(Ndm2)[0])
        NDM3=int(str(Ndm3)+str(Ndm2)+str(Ndm1)+"00")
        return(NDM3)
    #ND1()
    #ND2()
    #ND3()
    NMM1=ndom_add (ND1(), ND2())-2
    return(NMM1)