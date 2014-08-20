# ndom.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 29 March 2014

def ndom_to_decimal (a):
    d=0
    for i in range(len(str(a))):
        d+=int(str(a)[-(1+i)])*(6**i)
    return d

def decimal_to_ndom (a):
    d=""
    x=a
    while x>0:
        d+=str(x%6)
        x=x//6
    y=int(d[::-1])
    return y

def ndom_add (a, b):
    x=ndom_to_decimal (a)
    y=ndom_to_decimal (b)
    z=decimal_to_ndom (x+y)
    return z

def ndom_multiply (a, b):
    x=ndom_to_decimal (a)
    y=ndom_to_decimal (b)
    z=decimal_to_ndom (x*y)
    return z