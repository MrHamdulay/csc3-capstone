def ndom_to_decimal(x):
    y=0
    z=0
    d=str(x)
    d=d[len(d)-1]
    ndom=""
    if x>99:
        c=str(x)
        c=c[0]
        y=eval(c)
        y=y*36
        b=str(x)
        b=b[1]
        z=eval(b)
        z=z*6
        ee=y+z
        if int(d)!=0:
            ndom=ee+int(d)
            ndom=str(ndom)
        else:
            ndom=str(ee)+""
    elif x>=10:
        b=str(x)
        b=b[0]
        z=eval(b)
        z=z*6
        if int(d)!=0:
            ndom=str(z+int(d))+""
        else:
            ndom=str(z)+""
    else:
        ndom=d
    ndom=int(ndom)
    return ndom
def decimal_to_ndom(x):
    a=x%6
    b=x%36
    b=b//6
    c=x//36
    if c!=0:
        ndom=str(c)+str(b)+str(a)
    else:
        ndom=str(b)+str(a)
    return (ndom)        
def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a+b
    c=decimal_to_ndom(c)
    return c
def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a*b
    c=decimal_to_ndom(c)
    return c