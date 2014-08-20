# Martin Batek
# BTKMAR001
# 2 April 2014
# A program which can convert base-10 numbers to base-6 and back

import math

def ndom_to_decimal(a):
    x = str(a)
    num = 0
    for i in range(len(x)):
        num += (eval(x[len(x)-i-1])*6**i)
    return int(num)
# converts base-6 to base-10    
def decimal_to_ndom(a):
    def sixes(a):
        exponent = 0
        number = 0
        while number <= a:
            number = 6**exponent
            exponent += 1
        return number/6    
    # sixes: gives the highest root of six that is lower than a given number
    number = a
    remainder = 7
    ndom = 0
    while remainder >= 6:
        remainder = number%sixes(number)
        ndom += number//sixes(number)*(10**round(math.log(sixes(number),6)))
        number = remainder
        
    return int(ndom+remainder)
# converts base-10 to base-6
def ndom_add(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
# adds two ndom numbers and displays them in ndom
def ndom_multiply(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
# multiplies two ndom numbers and displays them in ndom
