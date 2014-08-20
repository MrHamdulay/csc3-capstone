def ndom_to_decimal(a):
    x=(a//100)*36+(a%100//10)*6+a%10
    return x

def decimal_to_ndom(a):
    unit=a%6
    tenth=(a%36)//6
    hundredth = a//36
    if hundredth == 0:
        hundredth=""
    if tenth==0 and hundredth==0:
        tenth=""
    x = str(hundredth)+str(tenth)+str(unit)
    eval(x)
    return x
    
def ndom_add(a,b):
    a_decimal=ndom_to_decimal(a)
    b_decimal=ndom_to_decimal(b)
    c=a_decimal+b_decimal
    return decimal_to_ndom(c)
    
def ndom_multiply(a,b):
    a_decimal=ndom_to_decimal(a)
    b_decimal=ndom_to_decimal(b)
    c=a_decimal*b_decimal
    return decimal_to_ndom(c)