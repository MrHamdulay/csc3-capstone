# Ndom arithmetic
# Kristin Kinmont
# 29 March 2014

def ndom_to_decimal(a):
    dec = eval(str(a)[0])
    length = len(str(a))
    for i in range(1,length):
        dec =6*dec
        dec += eval(str(a)[i]) 
    return dec

def decimal_to_ndom(a):
    unit = a
    ndom = ""
    while unit-1 >= 0:
        remainder = unit%6
        unit = unit//6
        ndom += str(remainder)
    ndom = eval(ndom[-1::-1])
    return ndom
    
def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    ab_sum = a + b
    ab_sum = decimal_to_ndom(ab_sum)
    return ab_sum

def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    ab_multiply = a * b
    ab_multiply = decimal_to_ndom(ab_multiply) 
    return ab_multiply