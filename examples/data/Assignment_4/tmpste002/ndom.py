__author__ = 'Stephen Temple'
__date__ = '2014/03/31'

def ndom_to_decimal(a):
    """Converts a Ndom number to decimal"""
    a = str(a)
    decimal = 0
    n = len(a)-1
    for i in a:
        decimal += int(i) * (6**n)
        n -= 1
    return decimal

def decimal_to_ndom(a):
    """Converts a decimal number to Ndom"""
    ndom = ''
    exp = 0
    while 6**exp <= a:
        exp += 1
    for i in range(exp, 0, -1):
        ndom += str(a // (6**(i-1)))
        a %= 6 ** (i-1)
    return int(ndom)


def ndom_add(a, b):
    """Adds 2 Ndom numbers"""
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a + b)


def ndom_multiply(a, b):
    """Multiples 2 Ndom numbers"""
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a * b)