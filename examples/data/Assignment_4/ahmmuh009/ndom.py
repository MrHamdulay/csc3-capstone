def ndom_to_decimal(a):
    exponent=0
    decimal=0
    a=str(a)
    for i in a[::-1]:
        decimal+=((int(i)*(6**exponent)))
        exponent+=1
    return decimal

def decimal_to_ndom(a):
    ndom = 0
    for i in range(0,len(str(a))+1,1):
        num=a%6
        ndom+=num*(10**i)
        a=a//6
    return ndom


def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    summation=a+b
    return decimal_to_ndom(summation)


def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    product=a*b
    return decimal_to_ndom(product)  
        
