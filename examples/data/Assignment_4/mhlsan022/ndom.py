'''I'm tryna make a function that converts scenary to decimal and decimal to scenary. Well not forgetting that it has to add scenary and also multiply it. Here goes nothing.
SANNDILE CHRISTOPHER MAHLANGU
3 April 2014'''
def decimal_to_ndom(num):
    sa=(num//36)
    q=((num-(36*sa))//6)
    unit=(num%6)
    list=[sa,q,unit]
    ndom=str(list[0]) + str(list[1]) + str(list[2])
    ndom=int(ndom)
    return ndom

def ndom_to_decimal(num):
    num =str(num)
    a = len(num)
    if a>1:
        q=6*eval(num[-2])
    else:
        q=0
    if a>2:
        sa= 36*eval(num[-3])
    else:
        sa=0
    unit=eval(num[-1])
    decimal =sa+q+unit
    return decimal

def ndom_add(ndom1,ndom2):
    ndom1 =ndom_to_decimal(ndom1)
    ndom2 =ndom_to_decimal(ndom2)
    sum_ndom =ndom1 + ndom2
    sum_ndom =decimal_to_ndom(sum_ndom)
    return sum_ndom

def ndom_multiply(ndom_1,ndom_2):
    ndom_1=ndom_to_decimal(ndom_1)
    ndom_2=ndom_to_decimal(ndom_2)
    product=ndom_1*ndom_2
    product=decimal_to_ndom(product)
    return product

