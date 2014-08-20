def ndom_to_decimal (a):
    if len(str(a)) == 1:
        x = a
    elif len (str(a)) == 2:
        a = str(a)
        p = a[:1]
        p = int(p)
        q = a[1:2]
        q = int(q)
        x = p*6 + q
    elif len (str(a)) == 3:
        a = str(a)
        p = a[:1]
        p = int(p)
        q = a[1:2]
        q = int(q)
        r = a[2:3]
        r = int(r)
        x = p*36 + q*6 + r
    return x

def decimal_to_ndom (a):
    if a <= 6:
        x = a
    elif a <= 36:
        p = a//6
        p = str(p)
        q = a%6
        q = str(q)
        x = p + q
    elif a <= 216:
        p = a//36
        p = str(p)
        a = a%36
        q = a//6
        q = str(q)
        r = a%6
        r= str(r)
        x = p + q + r
    elif a <= 1296:
        p = a//216
        p = str(p)
        a = a%216
        q = a//36
        q = str(q)
        a = a%36
        r = a//6
        r = str(r)
        s = a%6
        s = str(s)
        x = p + q + r + s
    elif a <= 7776:
        p = a//1296
        p = str(p)
        a = a%1296
        q = a//216
        q = str(q)
        a = a%216
        r = a//36
        r = str(r)
        a = a%36
        s = a//6
        s = str(s)
        t = a%6
        t = str(t)
        x = p + q + r + s + t
    elif a > 7776:
        p = a//7776
        p = str(p)
        a = a%7776
        q = a//1296
        q = str(q)
        a = a%1296
        r = a//216
        r = str(r)
        a = a%216
        s = a//36
        s = str(s)
        a = a%36
        t = a//6
        t = str(t)
        u = a%6        
        u = str(u)
        x = p + q + r + s + t + u
    return x
    
def ndom_add (a, b):
    x = ndom_to_decimal (a) + ndom_to_decimal (b)
    y = decimal_to_ndom (x)
    return y

def ndom_multiply (a, b):
    x = ndom_to_decimal (a)*ndom_to_decimal (b)
    y = decimal_to_ndom (x)
    return y