def ndom_to_decimal(a):
    total = 0
    unint = str(a)
    for i in range(len(unint)):
        power = (len(unint)-1-i)
        total += eval(unint[i])*6**power
    return total
    

def decimal_to_ndom (a):
    div = a
    rem = ""
    div2 = 1
    while div2 > 0:
        div2 = div//6
        rem += str(div%6)
        div = div2
    return rem[::-1]

def ndom_add (a,b):
    result = decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
    return result

def ndom_multiply (a, b):
    result = decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
    return result
        
        
        