def ndom_to_decimal(a):
    a=str(a)
    if len(a)==3:
        t=a[0]
        u=a[1]
        v=a[2]
        w=int(t)
        x=int(u)
        y=int(v)
        return(w*36+x*6+y*1)        
    elif len(a)==2:
        p=a[0]
        q=a[1]
        r=int(p)
        s=int(q)
        return(r*6+s*1)
    if len(a)==1:
        b=a[0]
        c=int(b)
        return(c*1)            
        
def decimal_to_ndom(a):
    b=str(a)
    if a<6:
        print(a)
    elif a>6:
        if len(b)==3:
            g=str(a//36)
            v=(a%36)
            h=str(v//6)
            j=str(a%6)
            k=int(g+h+j)
            return k
        if len(b)==2:
            g=str(a//36)
            v=(a%36)
            h=str(v//6)            
            e=str(a%6)
            f=int(g+h+e)
            return f
        if len(b)==1:
            x=int(a)
            return a
        
def ndom_add(a,b):
    ri=int(ndom_to_decimal(a))
    ro=int(ndom_to_decimal(b))
    x=ri+ro
    y=decimal_to_ndom(x)
    return y

def ndom_multiply(a,b):
    ra=int(ndom_to_decimal(a))
    re=int(ndom_to_decimal(b))
    l=ra*re
    q=decimal_to_ndom(l)
    return q
   
