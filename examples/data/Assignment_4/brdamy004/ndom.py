# Assignment 4 question 2
# Amy Brodie
# 2/04/2014

def ndom_to_decimal(a):
    s = str(a)
    e = len(s)-1
    decimal = 0
    for i in range(len(s)):
        n = eval(s[i])
        decimal += n*(6**e)
        e -= 1
    return decimal

def decimal_to_ndom(a):
    s = str(a)
    bndom = ""
    while a > 0:
        rem = a%(6)
        bndom += str(rem)
        a = a//6
    ndom = bndom[::-1] 
    return eval(ndom)

def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    c = a+b
    return decimal_to_ndom(c)

def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b) 
    c = a*b
    return decimal_to_ndom(c)