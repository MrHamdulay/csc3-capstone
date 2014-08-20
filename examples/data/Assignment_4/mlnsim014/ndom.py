def decimal_to_ndom(a):
    if 0<a<36:
        b = a%6
        c = a//6
        a = str(c) + str(b)
        a = int(a)
    

    elif a>=36:
        t= a%36
        u= t%6
        v = a//36
        x = t//6
        a= str(v) + str(x) + str(u)
        a = int(a)
    return a
def ndom_to_decimal(a):
    if 0<a<36:
        a = str(a)
        a = 6*int(a[0]) + int(a[1])
    elif a>= 36:
        a = str(a)
        a = 36*int(a[0]) + 6*(int(a[1])) + int(a[-1])
    return a

def ndom_add(a,b):
    a= ndom_to_decimal(a)
    b= ndom_to_decimal(b)
    sumN = a + b
    sumN = decimal_to_ndom(sumN)
    return sumN

def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    productN = a*b
    productN = decimal_to_ndom(productN)
    return productN