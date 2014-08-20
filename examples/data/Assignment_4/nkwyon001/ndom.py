
def ndom_to_decimal(a):
    x=str(a)
    if len(x)==1:
        s=a
        return s
    elif len(x)==2:
        xx=x[1]
        z=x[0] 
        p=eval(xx)
        pp=eval(z)
        o=p*(6**0)
        oo=pp*(6**1)
        d=o+oo
        return d
    elif len(x)==3:     
        xx=x[2]
        z=x[1] 
        w=x[0]
        j=eval(xx)
        jj=eval(z)
        jjj=eval(w)
        l=j*(6**0)
        ll=jj*(6**1)
        lll=jjj*(6**2)
        e=l+ll+lll
        return e
        
def decimal_to_ndom(a):
    y=a//6
    z=a%6
    yy=str(y)
    zz=str(z)
    w=yy+zz
    return w

def ndom_add(a,b):
    no=a+b
    return no

def ndom_multiply(a,b):
    nd=a*b
    return nd
    