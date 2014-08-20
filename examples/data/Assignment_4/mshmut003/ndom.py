def ndom_to_decimal(a):
    x=str(a)
    y = len(x)
    e=0
    for i in range(y):
        e+=eval(x[i])*6**(y-1-i)
    return e

def decimal_to_ndom(a):
    y=len(str(a))
    x=""
    for i in range(y):
        x+=str(a//6**(y-1))
        a=a%6**(y-1)
        y=y-1
    return x

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    x=a+b
    x=decimal_to_ndom(x)
    return x

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    x=a*b
    x=decimal_to_ndom(x)
    return x
    
    