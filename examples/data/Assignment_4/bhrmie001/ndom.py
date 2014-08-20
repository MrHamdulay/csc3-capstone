def decimal_to_ndom(a):
    dec=""
    while a/6!=0.0:
        b=a%6
        dec+=str(b)
        a=a//6
    dec=dec[::-1]
    dec=eval(dec)
    return dec

def ndom_to_decimal(a):
    a=str(a)
    b=len(a)-1
    ndom=0
    for i in a:
        i=eval(i)
        i=i*(6**b)
        ndom+=i
        b-=1
    return ndom

def ndom_add(a, b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))

def ndom_multiply(a, b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
