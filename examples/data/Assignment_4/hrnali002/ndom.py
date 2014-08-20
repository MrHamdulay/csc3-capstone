# A program for simple Ndom Arithmetic
# Alison Hoernle
# HRANLI002
# 1 April 2014

def ndom_to_decimal(a):
    # If a one digit number:
    if a < 6:
        dec = a
    
    # for two digit numbers:
    elif 10 <= a < 100: 
        mult = int(str(a)[0])
        dec = 6*mult + int(str(a)[1])
    
    # For a 3 digit number:
    elif 100 <= a:
        b = int(str(a)[0])*6
        c = b + int(str(a)[1])
        d = c*6
        e = d + int(str(a)[2])
        dec = e
        
    return dec
    
def decimal_to_ndom(a):
    # for numbers less than 6 (one digit ndom)
    if a < 6:
        ndom = a
        
    # for decimals that give two digit ndom numbers
    elif 6 <= a < 60:
        first = (int(a//6))
        second = int(a) - 6*int(first)
        ndom = str(first) + str(second)
        
    # for decimals that give three digit ndom numbers
    elif 60 <= a:
        b = int(a//6)
        c = int(b//6)
        ndom = str(c%6) + str(b%6) + str(a%6)
    
    return ndom
        
def ndom_add(a, b):
    
    # Change both numbers back to decimals
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    
    # Add the two numbers
    ans1 = a + b
    
    # Change the answer back to ndom
    ans2 = decimal_to_ndom(ans1)
    
    return ans2
    
def ndom_multiply(a, b):
    
    # Change both numbers to decimals
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    
    # Multiply them
    ans1 = a * b
    
    # Change the answer back to ndom
    ans2 = decimal_to_ndom(ans1)
    
    return ans2