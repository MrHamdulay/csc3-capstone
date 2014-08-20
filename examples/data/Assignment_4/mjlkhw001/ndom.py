# Module to use Ndom arithmetic
# Khwezi Majola
# MJLKHW001
# 31 March 2014

def ndom_to_decimal(a):
    b = str(a)
    i = len(b)
    x = 0
    for k in range(i):
        z = (b[k])
        z= int(z)
        x += z
        if k == (i-1):
            break
        x = (int(x) * 6)
    return x    

def decimal_to_ndom(a):
    x = ''
    k = len(x)-1
    z = a
    while True:
        b = z%6
        x += str(b)
        k -= -1
        z = z//6
        if z == 0:
            break    
    x = x[::-1]
    return x

def ndom_add(a, b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    result = x + y
    result = decimal_to_ndom(result)
    return result

def ndom_multiply(a, b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    result = x * y
    result = decimal_to_ndom(result)
    return result    