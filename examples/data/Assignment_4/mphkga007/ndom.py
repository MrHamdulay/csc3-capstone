#program tha converts decimal to base 6
#05/03/2014
#kkmphele


def decimal_to_ndom(decimal):
    decimal=int(decimal)
    ndom=""
    while  decimal>0:
        qoutient=decimal//6
        remainder=decimal%6
        remainder=str(remainder)
        ndom+=remainder
        decimal=qoutient
    ndom=ndom[::-1]
    ndom=int(ndom)
    
    return ndom



def ndom_to_decimal(ndom):
    ndom=str(ndom)
    zero=ndom[0]
    one=ndom[1]
    
    length=len(ndom)
    if length==2:
        zero=int(zero)
        one=int(one)
        ndom=int(ndom)
        decimal=(zero*6**1) + (one*6**0)
        
    elif length==3:
        zero=int(zero)
        one=int(one)
        two=ndom[2]
        two=int(two)
        ndom=int(ndom)
        decimal=zero*6**2 + one*6**1 + two*6**0

    return decimal

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    add=a+b
    answer=decimal_to_ndom(add)
    return answer

def ndom_multiply(a,b):
    
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    multiply=a*b
    answer=decimal_to_ndom(multiply)
    return answer    

        