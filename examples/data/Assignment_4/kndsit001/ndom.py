def ndom_to_decimal (a):
    a = str(a)
    b = len(a)-1
    d = 0
    for i in range(b,-1,-1):
        d = d + int(a[b-i])*6**i
    return(d)



def decimal_to_ndom (a):
    x = a//6**2
    b = a%6**2
    y = b//6**1
    c = b%6**1
    z = c//6**0
    d = str(x)+str(y)+str(z)
    return(int(d))



def ndom_add (a, b):
    m = ndom_to_decimal (a)
    n = ndom_to_decimal (b)
    o = m + n
    p = decimal_to_ndom (o)
    return(p)



def ndom_multiply (a, b):
    r = ndom_to_decimal (a)
    s = ndom_to_decimal (b)
    t = r*s
    u = decimal_to_ndom (t)
    return(u)
