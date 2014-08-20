def ndom_to_decimal (a):
    y=a%100
    z=y%10
    ans = ((a//100)*36)+((y//10)*6)+z
    return ans
def decimal_to_ndom (a):
    y=a%36
    z=y%6
    ans = ((a//36)*100)+((y//6)*10)+z
    return ans
def ndom_add (a, b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a+b
    return decimal_to_ndom(c)
def ndom_multiply (a, b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a*b
    return decimal_to_ndom(c)