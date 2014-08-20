def ndom_to_decimal(a):
    t=a
    r=0
    g=0
    while t!=0:
        r=r+(t%10)*(6**g)
        t=t//10
        g+=1
        
    return r


def decimal_to_ndom(a):
    t=a
    r=0
    g=0
    while t!=0:
        r+=(t%6)*(10**g)
        t=t//6
        g+=1
    return r

def ndom_add(a,b):
    w=ndom_to_decimal(a)
    x=ndom_to_decimal(b)
    z=w+x
    z=decimal_to_ndom(z)
    return z
    
def ndom_multiply(a,b):
    w=ndom_to_decimal(a)
    x=ndom_to_decimal(b)
    z=w*x
    u=decimal_to_ndom(z)
    return u