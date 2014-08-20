# Programs to perform simple Ndom arithmetic
# Nomsa Gamedze
# 1 April 2014

def ndom_to_decimal(a):
    a = str(a)
    if len(a) == 3:
        h = a[0:1]
        t = a[1:2]
        u = a[2:]
        h = int(h)
        t = int(t)
        u = int(u)
        h_dec = h*36
        t_dec = t*6
        u_dec = u
        dec_ans = h_dec + t_dec + u_dec
    if len(a) == 2:
        t = a[0:1]
        u = a[1:]        
        t = int(t)
        u = int(u)
        t_dec = t*6
        u_dec = u 
        dec_ans = t_dec + u_dec
    if len(a) == 1:
        u_dec = int(a)
        dec_ans = u_dec
    decimal = int(dec_ans)
    return decimal

def decimal_to_ndom(a):
    s = str(a)
    word = ""
    b = a/6
    c = a%6
    d = a//6
    e = d%6
    f = d//6
    g = f%6
    ndom = str(g) + str(e) + str(c)
    ndom = int(ndom)
    return ndom

def ndom_add(a, b):
    r = ndom_to_decimal(a)
    p = ndom_to_decimal(b)
    ans_dec = r + p
    ans_ndom = decimal_to_ndom(ans_dec)
    return ans_ndom

def ndom_multiply(a, b):
    q = ndom_to_decimal(a)
    w = ndom_to_decimal(b)
    ans_dec = q*w
    ans_ndom = decimal_to_ndom(ans_dec)
    return ans_ndom