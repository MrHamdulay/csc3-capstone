import math

def decimal_to_ndom(num):
    pow = int(math.log(num,6))
    sen = ''
    while pow>=0:
        dig = 6**pow
        mul = num//dig
        sen += str(mul)
        num -= mul*dig
        pow -= 1
    return int(sen)

def ndom_to_decimal(num):
    num = str(num)
    dec = 0
    length = len(num)
    for i in range(0,length):
        dec += int(num[i])*(6**(length-i-1))
    return dec

def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a+b)

def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a*b)