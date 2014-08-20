def ndom_to_decimal(a):
    a = str(a)
    ans=0
    
    if len(a)==3:
        b=2
        for i in range(3):
            x=int(a[i])*(6**b)
            ans+=x
            b-=1
        return ans
    
    elif len(a)==2:
        b=1
        for j in range(2):
            x=int(a[j])*(6**b)
            ans+=x
            b-=1
        return ans
    else:
        return a
    
def decimal_to_ndom(a):
    b=a//6
    c=a%6
    d=b//6
    e=b%6
    f=d%6
    h=""
    if f==0:
        m=str(e)
        n=str(c)
        h+=m+n
    else:
        m=str(f)
        n=str(e)
        o=str(c)
        h+=m+n+o
    return(int(h))
    
def ndom_add(a,b):
    import ndom
    a=ndom.ndom_to_decimal(a)
    b=ndom.ndom_to_decimal(b)
    c=a+b
    c=ndom.decimal_to_ndom(c)
    return c

def ndom_multiply(a,b):
    import ndom
    a=ndom.ndom_to_decimal(a)
    b=ndom.ndom_to_decimal(b)
    c=a*b
    c=ndom.decimal_to_ndom(c)
    return c
        
        