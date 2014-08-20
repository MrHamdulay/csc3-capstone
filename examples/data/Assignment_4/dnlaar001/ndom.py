def ndom_to_decimal (a):
    x=str(a)
    if len(x)==3:
    
        r=x[:1]
        b=x[1:2]
        c=x[2:]
        k=eval(r)
        j=eval(b)
        d=eval(c)
        h=k*36
        i=j*6
        l=h+i+d
        return l
    
    elif len(x)==2:
        r=x[:1]
        b=x[1:]
        k=eval(r)
        j=eval(b)
        i=r*6
        l=i+b
        return l  
    
    elif len(x)==1:
        h=eval(x)
        return h
    
def decimal_to_ndom (a):
    p=a//36
    q=a%36
    r=q//6
    s=q%6
    l=str(p)
    k=str(r)
    m=str(s)
    if l=='0':
        l=''
    if k=='0' and l=='0':
        k=''
    z=l+k+m
    y=eval(z)
    return y    

def ndom_add (a, b):
    v=ndom_to_decimal (a)
    w=ndom_to_decimal (b)
    g=v+w
    f=decimal_to_ndom (g)
    return f

def ndom_multiply (a, b):
    v=ndom_to_decimal (a)
    w=ndom_to_decimal (b)
    g=v*w
    f=decimal_to_ndom (g)
    return f    