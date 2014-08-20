import math
def decimal_to_ndom (a):
    y=str(a)
    ndom=""
    x=0
    decimal=int(y)
    while x<=len(y):
        lengte=len(y)
        base=6**(lengte-x)
        character=int(decimal/base)
        remainder=decimal%base
        character=str(character)
        ndom+=character
        x+=1
        decimal=remainder
    if ndom[0]=='0':
        ndom=ndom[1::1]
    else: ndom=ndom
    return int(ndom)





def ndom_to_decimal(a):
    x=str(a)
    if len(x)==3:
        first=6**2*int(x[0])
        second=6**1*int(x[1])
        third=6**0*int(x[2])
        decimal=first+second+third
    elif len(x)==2:
        first=6**1*int(x[0])
        second=6**0*int(x[1])
        decimal=first+second
    elif len(x)==1:
        first=6**0*int(x[0])
        decimal=first
    return int(decimal)
   


def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    decimal=x*y
    new_ndom=decimal_to_ndom(decimal)
    return int(new_ndom)



def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    decimal=x+y
    new_ndom=decimal_to_ndom(decimal)
    return int(new_ndom)



