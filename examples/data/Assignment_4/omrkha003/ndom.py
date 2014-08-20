# converts a Ndom number to decimal

def ndom_to_decimal(a) :
    
    x = 0
    y = 0
    a = str(a)
    
    for i in a[::-1] :
        num = eval(i)
        y = y + (num * (6**x))
        x = x + 1
    
    return y



#converts a decimal number to Ndom

def decimal_to_ndom(a) :
   
    z = 0
    w = len(str(a)) + 1
    
    for i in range(0, w) :
        rem = a % 6
        z = z + (rem * (10**i)) 
        a = a//6
        
    return z



# adds two Ndom numbers

def ndom_add(a, b) :
    
    a, b = ndom_to_decimal(a), ndom_to_decimal(b)
    sum = a + b
    
    return decimal_to_ndom(sum)



# multiplies 2 ndom numbers

def ndom_multiply(a, b) :
    
    a, b = ndom_to_decimal(a), ndom_to_decimal(b)
    product = a * b
    
    return decimal_to_ndom(product)