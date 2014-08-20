import math

def ndom_to_decimal (a):
    a = str(a)
    multi = 6**(len(a)-1)
    decimal = 0
    for i in a:
        y = eval(i)
        y = y * multi
        i = eval(i)
        decimal+=y
        multi//=6
        
    return decimal


def decimal_to_ndom (a):
    power = (math.log(a))/(math.log(6))
    power = int(power)
    num_of_digits = power + 1
    divisor = 6**(power)
    
    ndom=""
    x=a

    for i in range(num_of_digits):
        y= x%divisor
        digit = (x-y)//divisor
        digit = str(digit)
        ndom+=digit
        x = y
        divisor//=6
    
    ndom=eval(ndom)        
    return ndom
                
    
def ndom_add (a, b):
    z =  ndom_to_decimal(a) + ndom_to_decimal(b)
    y = decimal_to_ndom(z)
    return y


def ndom_multiply (a, b):
    z = (ndom_to_decimal(a)) * (ndom_to_decimal(b))
    y = decimal_to_ndom(z)
    return y