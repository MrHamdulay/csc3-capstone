def ndom_to_decimal(a):
    a=str(a)
    d=0
    for i in range(len(a)):
        d+=int(a[-i-1])*(6**i)
    return d

def decimal_to_ndom(a):
    d=str(a//36)
    d+=str((a%36)//6)
    d+=str(a%6)
    return int(d)    

def ndom_add(a,b):
    s=ndom_to_decimal(a)+ndom_to_decimal(b)
    return decimal_to_ndom(s)

def ndom_multiply(a,b):
    p=ndom_to_decimal(a)*ndom_to_decimal(b)
    return decimal_to_ndom(p)