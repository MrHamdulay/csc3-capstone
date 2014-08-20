# Conor O'Sullivan
# Convers to base 6 (visa versa)
# 4/01/2014

#ndom_to_decimal (a), that converts a Ndom number to decimal
def ndom_to_decimal(a):
    dec = 0
    for x in range(a+1):
        ndom = decimal_to_ndom(x)
        if ndom == a:
            dec = x
            break
    
    return dec
    
    
    
#decimal_to_ndom (a), that converts a decimal number to Ndom
def decimal_to_ndom(a):
    ndom = 0
    while a != 0:
        if a < 6:
            ndom += a
            a = 0
        elif a <36:
            num6 = (a//6)
            ndom = ndom + num6*10
            a -= num6*6
        elif a <216:
            num36 = (a//36)
            ndom = ndom + num36*100
            a -= num36*36
        elif a <1296:
                num216 = (a//216)
                ndom = ndom + num216*1000
                a -= num216*216  
    return ndom

    
#ndom_add (a, b), that adds 2 Ndom numbers
def ndom_add(a,b):
    a= ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    c = a + b
    c =  decimal_to_ndom(c)
    return c
    
#ndom_multiply (a, b), that multiples 2 Ndom numbers
def ndom_multiply(a,b):
    a= ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    c = a*b
    c =  decimal_to_ndom(c)
    return c