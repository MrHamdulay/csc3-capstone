def ndom_to_decimal(a):
    stra = str(a)
    decimals = 0
    for i in range (len(stra)):
        decimals = (decimals) + int(stra[i])
        decimals = decimals*6
        
    return decimals//6


def decimal_to_ndom(a):
    stra = str(a)
    sndom = ""
    for i in range (len(stra)+1):
        whole = a//6
        rem = a%6
        sndom = sndom + str(rem)
        a = whole
    sndom = sndom[::-1]
    return int(sndom)

def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    c = a+b
    return (decimal_to_ndom(c))

def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    c = a*b
    return (decimal_to_ndom(c))    
    
