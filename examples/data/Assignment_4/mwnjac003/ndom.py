def ndom_to_decimal (a):
    units = 0    
    tens = 0
    if len(str(a)) == 2:
        tens = str(a)[:1]
        tens = eval(tens)*6
        ans = tens + int(str(a)[1:])     
    if len(str(a)) == 3:
        thousand = str(a)[:1]
        thousand = eval(thousand)*36
        tens = str(a)[1:2]
        tens = eval(tens)*6
        ans = thousand + tens + int(str(a)[2:3])                                   
    if len(str(a)) == 1:
        ans = a
    return ans

def decimal_to_ndom (a):
    if  a >= 36:
        thousand = a//36
        tens = a-(thousand*36)
        tens = tens//6
        units = (a-(thousand*36))-(tens*6)
        ans = str(thousand) + str(tens) + str(units)
    if  6 <= a < 36:
        tens = a//6
        units = a-(6*tens)
        ans = str(tens) + str(units)
    if  0 < a < 6 :
        ans = a

    return ans    

def ndom_add (a, b):
    deci = (ndom_to_decimal(a)) + (ndom_to_decimal(b))
    answer = decimal_to_ndom(deci)
    return answer

def ndom_multiply (a, b):
    deci = (ndom_to_decimal(a)) * (ndom_to_decimal(b))
    answer = decimal_to_ndom(deci)
    return answer