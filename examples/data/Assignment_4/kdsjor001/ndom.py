def ndom_to_decimal(a):
    x=len(str(a))
    a=str(a)[::-1]
    d=0
    for i in range(x):
        f=int(a[i])*6**(i)
        d+=f
    return d

def decimal_to_ndom (a):
    ndom=0
    x=(len(str(a))+1)
    for i in range(x,-1,-1):
        while a>=6**i:
            a-=6**i
            ndom+=10**i
    return ndom
def ndom_add(a,b):
    c=ndom_to_decimal(a)+ndom_to_decimal(b)
    c=decimal_to_ndom(c)
    return(c)

def ndom_multiply(a,b):
    c=ndom_to_decimal(a)*ndom_to_decimal(b)
    c=decimal_to_ndom(c)
    return(c)