def ndom_to_decimal (a):
    q=str(a)
    b=len(q)
    d=0
    c= "invalid number"
    for i in range(b):
        if eval(q[i])>6:
            return c
        else:
            d+=(eval(q[i])*(6**(b-i-1)))
    return d

def decimal_to_ndom(a):
    q=str(a)
    b=2*len(q)
    d=""
    p=a
    while b>=0:
        t=a//(6**b)
        tp=p//(6**b)
        if t!=0:
            d+=str(tp)
            p=p-(tp*6**b)
        b=b-1 
    
    x=eval(d)
    return x

def ndom_add(a,b):
    x=ndom_to_decimal(a)+ndom_to_decimal(b)
    y=decimal_to_ndom(x)
    return y

def ndom_multiply(a,b):
    x=ndom_to_decimal(a)*ndom_to_decimal(b)
    y=decimal_to_ndom(x)
    return y