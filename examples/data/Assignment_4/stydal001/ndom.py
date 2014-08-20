# Dalise Steynfaard
# STYDAL001
# Assignment 4, question 2
# 03-04-2014

def ndom_to_decimal(a):
    list_a = list(str(a))
    length_a = len(str(a))
    ndom_a = 0
    
    for i in range(length_a):
        list_a[-1-i] = int(list_a[-1-i]) * (6**i)
        
    for j in list_a:
        ndom_a += int(j)
    
    return ndom_a

def decimal_to_ndom(a):
    list_a = []
    length_a = len(str(a))
    decimal_a = ''
    
    while length_a >= 0:
        list_a.append(str(a//6**length_a))
        a = a % 6**length_a
        length_a -= 1
    
    for j in list_a:
        decimal_a += j

    return int(decimal_a)

def ndom_add(a,b):
    dec_a, dec_b = ndom_to_decimal(a), ndom_to_decimal(b)
    add_ab = dec_a + dec_b
    ndom_ab = decimal_to_ndom(add_ab)
    
    return ndom_ab
    
def ndom_multiply(a,b):
    dec_a, dec_b = ndom_to_decimal(a), ndom_to_decimal(b)
    add_ab = dec_a * dec_b
    ndom_ab = decimal_to_ndom(add_ab)
    
    return ndom_ab