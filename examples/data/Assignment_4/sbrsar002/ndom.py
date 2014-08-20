



def ndom_to_decimal(a):
    b=str(a)
    ans=0
    
    if len(b)==3:
        c=2
        for i in range(3):            
            x=int(b[i]) * (6**c)
            ans+=x
            c-=1            
        return ans
    
    elif len(b)==2:
        c=1
        for j in range(2):
            x=int(b[j]) * (6**c)
            ans+=x
            c-=1
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
        p=str(e)
        r=str(c)
        h+=p+r
    else:
        p=str(f)
        r=str(e)
        l=str(c)
        h+=p+r+l
    return(int(h))  
 

def ndom_add(a,b):
    import ndom
    a=ndom.ndom_to_decimal (a)
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
            