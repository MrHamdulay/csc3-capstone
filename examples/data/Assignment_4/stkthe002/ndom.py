
def ndom_to_decimal (a):
    decimal = 0
    ndom = str(a)
    for i in range(len(ndom)):
        power = len(ndom)-(i+1)
        decimal += int(ndom[i])*(6**power)
    return decimal

def decimal_to_ndom(a): #integer
    if a == 0:
        return 0
    value = '' #string
    while a > 0: #det fortsatt er rest
        value += str(a%6) #forste siffer er rest av foregaaende delestykke
        a = a//6
    value = value[::-1]
    return value
    
def ndom_add (a,b):
    length = max(len(str(a)), len(str(b)))
    result = ''
    value = 0
    
    a = str(a).zfill(length)
    b = str(b).zfill(length)    
    
    for i in range(length-1,-1,-1):
        c = int(str(a)[i]) + int(str(b)[i]) + value
        if c >= 6:
            c -= 6
            value = 1
            link = str(c)
            result += link
            
        else:
            link = str(c)
            result += link
            value = 0
            
    result = result[::-1]
    return result  
    
def ndom_multiply(a,b):
    a = ndom_to_decimal (a)
    b = ndom_to_decimal (b)
    factor = a*b
    factor = decimal_to_ndom(factor)
    return factor
    

    
        
#123 = 1*10^2 + 2*10^1 +3*10^0 = 123
#123 = 1*6^2  + 2*6^1  +3*6^0  = 55
        