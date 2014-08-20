


def decimal_to_ndom(a):
    base = 6
    ndom = ""
    
 
    while a:
        mod = a % base
        a = a // base
        ndom = chr(48 + mod + 7*(mod > 10)) + ndom
    return ndom

        
        
def ndom_to_decimal(a):
    astr = str(a)
    if len(astr) == 3:
        t1 = eval(astr[0])
        t2 = eval(astr[1])
        t3 = eval(astr[2])
        decimal = t1*36 + t2*6 + t3
        return decimal
    elif len(astr) == 2:
        t1 = eval(astr[0])
        t2 = eval(astr[1])
        decimal = t1*6 + t2
        return decimal
    elif len(astr) == 1:
        decimal = a
        return decimal
    
    
def ndom_add(a,b):
    decimal_awnser = ndom_to_decimal(a) + ndom_to_decimal(b)
    return decimal_to_ndom(decimal_awnser)

def ndom_multiply(a,b):
    decimal_awnser = ndom_to_decimal(a)*ndom_to_decimal(b)
    return decimal_to_ndom(decimal_awnser)
    