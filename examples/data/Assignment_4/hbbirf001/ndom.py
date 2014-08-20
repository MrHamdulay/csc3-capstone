# nDom Converter
# Irfan Habib
# 3 April 2014

def ndom_to_decimal(a):
    i = 0
    y=0
    a = str(a)
    for x in a[::-1]:
        y+= ((eval(x)*(6**i)))
        i += 1
    return y

def decimal_to_ndom(a):
    f = 0
    for i in range(0,len(str(a))+1,1):
        r = a%6
        f+=r*(10**i)
        a =a//6
    return f

def ndom_add(a,b):
    a,b = ndom_to_decimal(a),ndom_to_decimal(b)
    c = a+b
    return decimal_to_ndom(c)

def ndom_multiply(a,b):
    a,b = ndom_to_decimal(a),ndom_to_decimal(b)
    c = a*b
    return decimal_to_ndom(c)    
    