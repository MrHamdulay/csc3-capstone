def ndom_to_decimal(a):
    a = str(a)[::-1]
    dec = 0
    i = 0
    while i < len(a):
        dec = dec + eval(a[i]) * 6 ** i
        i = i + 1
    return dec

def decimal_to_ndom(a):
    ndom = ""
    while a > 0:
        ndom += str(a % 6)
        a = a // 6
    ndom = ndom[::-1]
    return eval(ndom)

def ndom_add(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) + ndom_to_decimal(b))

def ndom_multiply(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) * ndom_to_decimal(b))
