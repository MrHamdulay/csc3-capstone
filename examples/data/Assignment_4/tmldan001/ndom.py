__author__ = 'Daniel'
def decimal_to_ndom(num):
    ndom=0
    t=num
    for i in range(0,len(str(num))+1):
        r=t%6
        ndom += r*(10**i)
        t = t//6
    return ndom

def ndom_to_decimal(num):
    decimal=0
    t=num
    for i in range (0,len(str(num))):
        r=t%10
        decimal += r*(6**i)
        t=t//10
    return decimal

def ndom_add(a,b):
    x = ndom_to_decimal(a)+ndom_to_decimal(b)
    return decimal_to_ndom(x)

def ndom_multiply(a,b):
    x= ndom_to_decimal(a)*ndom_to_decimal(b)
    return decimal_to_ndom(x)