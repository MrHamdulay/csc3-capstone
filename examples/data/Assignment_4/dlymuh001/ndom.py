def ndom_to_decimal(a):
    dec = 0
    i = 0
    while a > 0:
        digit = a % 10
        dec += (6**i) * digit
        a = a // 10
        i += 1
    return dec

def decimal_to_ndom(a):
    ndom = 0
    i = 0
    while a > 0:
        digit = a % 6
        ndom += digit * (10**i)
        a = a // 6
        i += 1
    return ndom

def ndom_add(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) + ndom_to_decimal(b))

def ndom_multiply(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) * ndom_to_decimal(b))