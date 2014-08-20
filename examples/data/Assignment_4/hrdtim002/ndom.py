"""converting base 10 and base 6 integers
tim hardie
1/4/14"""

def decimal_to_ndom(n):
    count=len(str(n))
    ndom = str(n%6)
    for i in range(count):
        n//=6
        ndom = str(n%6) + ndom
    ndom = int(ndom)
    return ndom

def ndom_to_decimal(n):
    count = len(str(n))
    dec = 0
    for i in range(count):
        if (int(str(n)[i])) > 5:
            return "invalid"
        dec += (int(str(n)[i]))*(6**(count-i-1))
    return dec

def ndom_add(num1, num2):
    sum = ndom_to_decimal(num1) + ndom_to_decimal(num2)
    return decimal_to_ndom(sum)

def ndom_multiply(num1, num2):
    product = ndom_to_decimal(num1) * ndom_to_decimal(num2) 
    return decimal_to_ndom(product)