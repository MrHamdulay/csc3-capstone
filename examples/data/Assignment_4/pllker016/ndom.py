def ndom_to_decimal(a):
    
    str_a = str(a)
    decimal = 0
    
    if len(str_a) == 3:
        hundreds = eval(str_a[0]) 
        tens = eval(str_a[1]) 
        units = eval(str_a[2]) 
        decimal = hundreds*36+tens*6+units
       
        
    elif len(str(a)) == 2:
        tens = eval(str_a[0]) 
        units = eval(str_a[1]) 
        decimal = tens*6+units
        
    elif len(str(a)) == 1:
        decimal = a
    
    return decimal
        

def decimal_to_ndom(a):
    ndom = ""
    if a >= 36:
        hundreds = a//36
        tens = (a-hundreds*36)//6
        units = a - (hundreds*36) - tens*6
        ndom = str(hundreds)+str(tens)+str(units)
       
        
    elif a >= 6:
        tens = a//6
        units = a - (tens*6)
        ndom = str(tens)+str(units)
        
    elif a < 6:
        ndom = a
        
    return ndom

def ndom_add(a, b):
    decimal_a = ndom_to_decimal(a)
    decimal_b = ndom_to_decimal(b)
    
    decimal_sum = decimal_a + decimal_b
    
    ndom_sum = decimal_to_ndom(decimal_sum)
    
    return ndom_sum

def ndom_multiply(a, b):
    decimal_a = ndom_to_decimal(a)
    decimal_b = ndom_to_decimal(b)
        
    decimal_product = decimal_a * decimal_b
        
    ndom_product = decimal_to_ndom(decimal_product)
        
    return ndom_product
    