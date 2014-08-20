def ndom_to_decimal (a):
    ten = False
    b = 0
    count = 0
    while a:
        if a%10 == 0 and count == 0:
            ten = True
            
        b = b*10 + a%10
        a = a//10
        count+=1
        
    ndom = 0    
    while b:
        ndom = ndom*6 + b%10
        b = b//10
        
    if ten == True:
        return ndom*6
    else:
        return ndom

def decimal_to_ndom (a):
    six = False    
    b = 0
    count = 0
    while a:
        if a%6 == 0 and count == 0:
            six = True
            
        b = b*10 + a%6
        a = a//6
        count+=1

    decimal = 0
    while b:
        decimal = decimal*10 + b%10
        b = b//10
        
    if six == True:
        return decimal*10
    else:    
        return decimal

def ndom_add (a, b):
    sum = ndom_to_decimal(a) + ndom_to_decimal(b)
    return decimal_to_ndom(sum)

def ndom_multiply (a, b):
    multiple = ndom_to_decimal(a) * ndom_to_decimal(b)
    return decimal_to_ndom(multiple)    