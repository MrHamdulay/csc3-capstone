#Phumelele Ndimande
#Assignment 4

def ndom_to_decimal(a):
    decimal = 0
    string = str(a)
    length = len(string)
    for i in range(length):
        decimal = decimal + eval(string[i])
        decimal *= 6
    
    decimal //= 6    
         
    return (decimal)

def decimal_to_ndom(a):
    decimal = a
    ndom = ''
    while decimal > 0:
        remainder = decimal%6
        ndom = str(remainder) + ndom
        decimal = decimal//6
        
    return (ndom)

def ndom_add (a, b):
    A = ndom_to_decimal(a)
    B = ndom_to_decimal(b)
    A = A + B
    
    C = decimal_to_ndom(A)
    return (C)

def ndom_multiply (a, b): 
    A = ndom_to_decimal(a)
    B = ndom_to_decimal(b)
    A = A * B
    
    C = decimal_to_ndom(A)
    return eval(C)     
