def ndom_to_decimal(a):
    num=(a//100)*36+(a%100//10)*6+a%10
    return num

def decimal_to_ndom(a):
    u=a%6
    t=(a%36)//6
    h = a//36
    if h == 0:
        h=""
    if t==0 and h==0:
        t=""
    num = str(h)+str(t)+str(u)
    eval(num)
    return num
    
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