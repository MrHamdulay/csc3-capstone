'''Sanele Mdlalose
MDLSAN019
Question3,Assignement4
A program that converts Ndom numbers to decimal numbers and vise versa
03 April 2014'''

def decimal_to_ndom(deci):
    q = deci
    ndom_no = ''
    while q:
        r = q%6
        q = q//6
        ndom_no += str(r)
    ndom = int(ndom_no[::-1])
    return ndom    
    
def ndom_to_decimal(n):
    n = str(n)
    suM = 0
    for i in range(len(n)):
        lastDigit = int(n[-1])
        n = n[0:-1]
        suM += (lastDigit*(6**i))
    return suM
    
def ndom_add(a,b):
    sum_dec = (ndom_to_decimal(a))+(ndom_to_decimal(b))
    sum_ndom = decimal_to_ndom(sum_dec)
    return sum_ndom

def ndom_multiply(a,b):
    product_dec = (ndom_to_decimal(a))*(ndom_to_decimal(b))
    product_ndom = decimal_to_ndom(product_dec)
    return product_ndom
