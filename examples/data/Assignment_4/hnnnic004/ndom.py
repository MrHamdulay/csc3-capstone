#ndom converter
#nicole henning
#due: 04/04/14

#unit digit leave 6^0
#tens digit times by 6^1
#hundreds digit times by 6^2import math

import math

def ndom_to_decimal (a):
    #converting ndom to decimal
    decimal = 0
    number_str = str(a)
    converter = 6**(len(number_str)-1)
    
    for i in number_str:
        number_int = eval(i)
        number_int = number_int * converter
        i = eval(i)
        decimal+=number_int
        converter//=6
      
    return decimal 
#successful


def decimal_to_ndom (a):
    # from decimal to ndom
    ndom=""
    
    exponent = (math.log(a))/(math.log(6))
    exponent = int(exponent)
    num_of_digits = exponent + 1 #used later for range
    denom = 6**(exponent)
   
    x=a
    
    for i in range(num_of_digits):
        y= x % denom
        digit = (x-y)//denom
        digit = str(digit)
        ndom += digit
        x = y
        denom = denom//6   

    ndom=eval(ndom)
    
    return ndom
    

def ndom_add (a, b):
    #convert to dec then add, then convert back
    dec_sum =  ndom_to_decimal(a) + ndom_to_decimal(b)
    ndom_sum = decimal_to_ndom(dec_sum)
    return ndom_sum


def ndom_multiply (a, b):
    #convert to dec then multiply, then convert back
    dec_product = (ndom_to_decimal(a)) * (ndom_to_decimal(b))
    ndom_product = decimal_to_ndom(dec_product)
    return ndom_product