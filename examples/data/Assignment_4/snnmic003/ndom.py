# Michael Sanne
# 2014/03/31
# Question 2

def decimal_to_ndom (a):
    hundreds = (a//36)
    a -= hundreds*36
    tens = (a//6)
    units = a-(tens*6)
    return (hundreds*100 + tens*10 + units)
    
def ndom_to_decimal (a):
    hundreds = a//100
    tens = (a - (hundreds*100))//10
    units = (a - hundreds*100 - tens*10)
    
    hundreds *= 36
    tens *= 6
    sum = hundreds + tens + units
    return sum
    
def ndom_add (a, b):
    a = ndom_to_decimal (a)
    b = ndom_to_decimal(b)
    sum = a+b
    sum = decimal_to_ndom(sum)
    return sum
        
def ndom_multiply (a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    
    product = a*b
    product = decimal_to_ndom(product)
    return product