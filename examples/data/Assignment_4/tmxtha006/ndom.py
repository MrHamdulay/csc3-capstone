"""Hebert TEMA
TMXTHA006
3 APRIL 2014
this program prints out boxes on screen in three different ways"""

def ndom_to_decimal(a):
    e=0                    #where e is an exponent of base 
    parts=0
    for i in (str(a))[::-1]:
        parts+=(int(i)*(6**e))
        e+=1
    return parts
    #print(parts)
#ndom_to_decimal(a)
    
def decimal_to_ndom(a):
    d=a
    r=""
    while d>6:
        r+=str(d%6)
        d//=6
    r+=str(d)
    ndom=int(r[::-1])
    return ndom
#decimal_to_ndom(a)
        
def ndom_add(a,b):
    A=ndom_to_decimal(a)
    B=ndom_to_decimal(b)
    x=A+B
    sum_ab=decimal_to_ndom(x)
    return sum_ab
    #ndom_add(a,b)
    
def ndom_multiply(a, b):
    A=ndom_to_decimal(a)
    B=ndom_to_decimal(b)
    x=A*B
    product_ab=decimal_to_ndom(x)
    return product_ab    
    #ndom_multiply(a, b)   
    