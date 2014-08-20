
def decimal_to_ndom(a):
    myout = ''
    while a != 0:
        myout = str(a % 6) + myout
        a //= 6
    return int(myout)

def ndom_to_decimal(a):
    myout = 0
    for i in range(len(str(a))):
        myout += int(str(a)[i]) * 6**(len(str(a)) - i - 1)
    return myout

def ndom_add (a, b):
    return decimal_to_ndom(ndom_to_decimal(a) + ndom_to_decimal(b))

def ndom_multiply(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) * ndom_to_decimal(b))
    
