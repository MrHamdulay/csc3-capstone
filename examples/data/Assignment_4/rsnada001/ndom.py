def ndom_to_decimal(a):
    a = str(a)
    number = 0
    for i in range(len(a)-1,-1,-1):
        number += int(a[len(a)-1-i])*6**(i)
    return number
def decimal_to_ndom(a):
    number = ''
    while a != 0:
        number += str(a%6)
        a = a//6
    return int(number[::-1])
def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a+b)
def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a*b) 
