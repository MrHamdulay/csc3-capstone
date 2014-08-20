#Assignment 4
#Question 2
#Rabia Parker

import math

def ndom_to_decimal (a):
    a=str(a)
    multi=6**(len(a)-1)
    decimal=0
    for i in a:
        y=eval(i)
        y=y*multi
        i=eval(i)
        decimal=decimal+y
        multi=multi//6
    return decimal

def decimal_to_ndom(a):
    p=(math.log(a))/(math.log(6))
    p=int(p)
    num=p + 1
    divisor=6**(p)
    ndom=""
    x=a
    for i in range(num):
        y=x%divisor
        number=(x-y)//divisor
        number=str(number)
        ndom=ndom+number       
        x=y
        divisor=divisor//6
    ndom=eval(ndom)        
    return ndom
    
def ndom_add (a, b):
    z=ndom_to_decimal(a) + ndom_to_decimal(b)
    y=decimal_to_ndom(z)
    return y

def ndom_multiply (a, b):
    z=(ndom_to_decimal(a)) * (ndom_to_decimal(b))
    y=decimal_to_ndom(z)
    return y
