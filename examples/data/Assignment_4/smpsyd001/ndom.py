def ndom_to_decimal(num):
    if num >60:
        a=int(num/100)
        b=int((num-a*100)/10)
        c=int(num-a*100-b*10)
        num=a*36+6*b+c
        return num
    elif num >6:
        b=int(num/10)
        c=int(num-b*10)
        num=6*b+c
        return num
    elif num<=6:
        return num

def decimal_to_ndom(num):
    if num>=42:
        a=num//36
        b=num%36
        c=b//6
        d=b%6
        num=a*100+c*10+d
        return num
    elif num>6:
        c=num//6
        d=num%6
        num=c*10+d
        return num
    else:
        return num
    
def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    c=x+y
    c=decimal_to_ndom(c)
    return c

def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    c=x*y
    c=decimal_to_ndom(c)
    return c    