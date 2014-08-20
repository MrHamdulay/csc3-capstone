def decimal_to_ndom(a):
    answer=a
    remainder1=""
    while answer>0:
        remainder=answer%6
        c=str(remainder)
        remainder1+=c
        #print(remainder)
        answer=answer//6  # updating answer
    d=remainder1[::-1]
    return d
def ndom_to_decimal(b):
    c=str(b)
    d=len(c)
    if d==3:
        e=c[0]
        f=c[1]
        g=c[2]
        k=int(e)*6**2+int(f)*6**1+int(g)*6**0
        return k
    if d==2:
        h=c[0]
        j=c[1]
        l=int(h)*6**1+int(j)*6**0
        return l
    else:
        return b
def ndom_add(x,z):
    y=ndom_to_decimal(x)
    t=ndom_to_decimal(z)
    s=y+t
    r=decimal_to_ndom(s)
    return r
def ndom_multiply(m,n):
    p=ndom_to_decimal(m)
    q=ndom_to_decimal(n)
    v=p*q
    u=decimal_to_ndom(v)
    return u
    
    