def ndom_to_decimal(a):
    a = str(a)
    b = list(map(int,str(a)))
    if 5>=int(a)>=0:
        return (int(a))
    else:
        multi=6
        x = 0
        y = 1
        track= b[0]
        for i in range (len(a)-1):
            dec = track*multi + (b[y])
            y=y+1
            track = dec
        newvalue = int(dec)
        return (newvalue) 

def decimal_to_ndom (a):
    numbers = '0123456789'
    y = ''
    while 1:
        x = a%6
        y = numbers[x] + y
        a = a//6
        if a ==0:
            break
    ndom = eval(y)
    return ndom

def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z = x+y
    e = decimal_to_ndom(z)
    return e

def ndom_multiply(a,b):
    r = ndom_to_decimal(a)
    t = ndom_to_decimal(b)
    q = r*t
    m = decimal_to_ndom(q)
    return m
