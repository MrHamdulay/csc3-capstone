
def ndom_to_decimal (a):
    a=str(a)
    a=int(a,6)
    return(a)


def decimal_to_ndom (a):
    bmod=a%6
    b=a//6
    cmod=b%6
    c=b//6
    dmod=c%6
    d=c//6
    emod=d%6
    e=d//6
    a=str(emod)+str(dmod)+str(cmod)+str(bmod)
    a=int(a)
    return(a)

def ndom_add (a,b):
    a=str(a)
    b=str(b)
    a=int(a,6)
    b=int(b,6)
    a=a+b
    bmod=a%6
    b=a//6
    cmod=b%6
    c=b//6
    dmod=c%6
    d=c//6
    emod=d%6
    e=d//6
    a=str(emod)+str(dmod)+str(cmod)+str(bmod)
    a=int(a)
    return(a)    


def ndom_multiply (a,b):
    a=str(a)
    b=str(b)
    a=int(a,6)
    b=int(b,6)
    a=a*b
    bmod=a%6
    b=a//6
    cmod=b%6
    c=b//6
    dmod=c%6
    d=c//6
    emod=d%6
    e=d//6
    a=str(emod)+str(dmod)+str(cmod)+str(bmod)
    a=int(a)
    return(a)
    

    




    
