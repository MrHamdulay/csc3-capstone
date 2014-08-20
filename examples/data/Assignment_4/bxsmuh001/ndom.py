def decimal_to_ndom(a):
    if a == 0:
        return 0
    result = ""
    while a > 0:
        result = str(a%6) + result
        a //= 6
    return (result)

def ndom_to_decimal(a):
    result = int(str(a), 6)
    return result

def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)    
    decimal = a + b
    senary = decimal_to_ndom(decimal)
    return (senary)

def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)    
    decimal = a * b
    senary = decimal_to_ndom(decimal)
    return (senary)