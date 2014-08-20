def decimal_to_ndom(a):
    ndomnum=""     
    while a>0:
        y=a%6        
        ndomnum+=str(y)
        a=a//6
    ndomnum=ndomnum[::-1]
    return int(ndomnum)

def ndom_to_decimal(a):
    ndom=0
    l=len(str(a))
    a=str(a)
    p=l-1
    for i in range(l):
        x=int(a[i])*(6**p)
        p+=-1
        ndom=ndom+x
    return ndom

def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x+y
    ndom=decimal_to_ndom(z)
    return ndom

def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x*y
    ndom=decimal_to_ndom(z)
    return ndom

        
        
        
        
        
    

    
        
        
        
        
        
        
        