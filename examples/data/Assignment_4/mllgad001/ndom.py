def ndom_to_decimal(a):
    a = str(a)
    x = 0
    n = 0
    for i in a[::-1]:
        square = 6**x
        n = n + (eval(i)*square)
        x = x + 1
    return n

def decimal_to_ndom(a):
    x=0
    length = len(str(a))
    for i in range(0, length+1, 1):
        y = a%6
        square = 10**i
        x = x+y*(square)
        a = a//6
    return x

def ndom_add(a,b):
    a,b = ndom_to_decimal(a),ndom_to_decimal(b)
    x = a+b
    return decimal_to_ndom(x)

def ndom_multiply(a,b):
    a,b = ndom_to_decimal(a), ndom_to_decimal(b)
    x = a*b
    return decimal_to_ndom(x)