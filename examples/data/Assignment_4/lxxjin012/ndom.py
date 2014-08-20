def ndom_to_decimal (a):
    x=str(a)
    if len(str(a))==1:
        digit1=int(str(a)[0])*1
        number=digit
    elif len(str(a))==2:
        digit2=int(str(a)[0])*6
        digit3=int(str(a)[1])*1
        number=digit2+digit3
    elif len(str(a))==3:
        digit4=int(str(a)[0])*36
        digit5=int(str(a)[1])*6
        digit6=int(str(a)[2])*1
        number=digit4+digit5+digit6
    return number
    
def decimal_to_ndom (a):
    digit1=a//36
    b=a-(digit1*36)
    digit2=b//6
    c=b-(digit2*6)
    number=(digit1*100)+(digit2*10)+(c)
    return number

def ndom_add (a, b):
    add=ndom_to_decimal(a)+ndom_to_decimal(b)
    ndom=decimal_to_ndom (add)
    return ndom
    
def ndom_multiply(a,b):
    multiply=(ndom_to_decimal(a))*(ndom_to_decimal(b))
    ndom=decimal_to_ndom (multiply)
    return ndom