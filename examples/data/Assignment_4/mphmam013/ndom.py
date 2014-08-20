def ndom_to_decimal(a):
    strN=str(a)
    length=len(strN)
    Bs=0
    for i in range(0,length):
        n=strN[i:i+1]
        p=length-(i+1)
        b6 = (int(n))*(6**p)
        Bs=Bs+b6
    return Bs

def decimal_to_ndom(a):
    length=len(str(a))
    na=""
    t=int(a)
    for i in range(0,(length+1)):
        b6=6**(length-i)
        n=t//b6
        d=n*b6
        t=t-d
        if(i>0) or (n!=0):
            na=na+str(n)
    return na

def ndom_add(n1,n2):
    m1=int(ndom_to_decimal(n1))
    m2=int(ndom_to_decimal(n2))
    t=m1+m2
    sum = decimal_to_ndom(str(t))
    return sum

def ndom_multiply(n1,n2):
    m1=int(ndom_to_decimal(n1))
    m2=int(ndom_to_decimal(n2))
    t=m1*m2
    multi = decimal_to_ndom(str(t))
    return multi    
