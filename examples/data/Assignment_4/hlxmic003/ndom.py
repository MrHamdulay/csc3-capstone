# Michaela Heale
# Assignment 4 Question 2

import math

def ndom_to_decimal(a):
    stra = str(a)
    lng = len(stra)
    newnumb = 0
    for z in range (0,lng,1):
        first = int(stra[z])
        power = math.pow(6,(lng-1-z))
        no6 = first*power
        newnumb += no6
    red = int(newnumb)
    return red

def decimal_to_ndom(a):
    stra = str(a)
    lng = len(stra)
    newnumb = ""
    rem = a
    for z in range(0,lng,1):
        power = math.pow(6,(lng-z))
        no10 = rem//power
        rem -= (no10*power)
        str10 = str(int(no10))
        newnumb += str10 +""
    strem = str(rem)
    newnumb += strem +""
    red = int(eval(newnumb))
    return red

def ndom_add(a,b):
    deca = int(ndom_to_decimal(a))
    decb = int(ndom_to_decimal(b))
    
    decatote = deca + decb
    ndomtote = decimal_to_ndom(decatote)
    return ndomtote
 
def ndom_multiply(a,b):
    deca = ndom_to_decimal(a)
    decb = ndom_to_decimal(b)
        
    decatote = deca * decb
    ndomtote = decimal_to_ndom(decatote)    
    return ndomtote