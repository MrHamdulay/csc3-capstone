def ndom_to_decimal(f):
    strN1=str(f)
    length=len(strN1)
    Bs1=0
    for i in range(0,length):
        u=strN1[i:i+1]
        p1=length-(i+1)
        b6 = (int(u))*(6**p1)
        Bs1=Bs1+b6
    return Bs1

def decimal_to_ndom(f):
    length=len(str(f))
    na1=""
    t1=int(f)
    for i in range(0,(length+1)):
        b6=6**(length-i)
        u=t1//b6
        d1=u*b6
        t1=t1-d1
        if(i>0) or (u!=0):
            na1=na1+str(u)
    return na1

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
