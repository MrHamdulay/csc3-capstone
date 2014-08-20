
def decimal_to_ndom(a):
    x = ''
    while a != 0:
        x = str(a % 6) + x
        a //= 6
    return int(x)

def ndom_to_decimal(a):
    x = str(a)
    myout = 0
    for i in range(len(x)):
        myout += int(x[i]) * 6**(len(x) - i - 1)
    return myout

def ndom_add (a, b):
    return decimal_to_ndom(ndom_to_decimal(a) + ndom_to_decimal(b))

def ndom_multiply(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) * ndom_to_decimal(b))
    
