def ndom_to_decimal(a):
    number=(a//100)*36+(a%100//10)*6+a%10
    return number

def decimal_to_ndom(a):
    unit=a%6
    ten=(a%36)//6
    hundreds = a//36
    if hundreds == 0:
        hundreds=""
    if ten==0 and hundreds==0:
        ten=""
    number = str(hundreds)+str(ten)+str(unit)
    eval(number)
    return number
    
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