def ndom_to_decimal(a):
    
    strA = str(a)
    decimal = 0
    
    if len(strA) == 3:
        h_digit = eval(strA[0]) 
        t_digit = eval(strA[1]) 
        u_digit = eval(strA[2]) 
        decimal = h_digit*36+t_digit*6+u_digit
       
        
    elif len(str(a)) == 2:
        t_digit = eval(strA[0]) 
        u_digit = eval(strA[1]) 
        decimal = t_digit*6+u_digit
        
    elif len(str(a)) == 1:
        decimal = a
    
    return decimal
        

def decimal_to_ndom(a):
    ndom = ""
    if a >= 36:
        h_digit = a//36
        t_digit = (a-h_digit*36)//6
        u_digit = a - (h_digit*36) - t_digit*6
        ndom = str(h_digit)+str(t_digit)+str(u_digit)
       
        
    elif a >= 6:
        t_digit = a//6
        u_digit = a - (t_digit*6)
        ndom = str(t_digit)+str(u_digit)
        
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
    