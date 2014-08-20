def decimal_to_ndom(n):
    t36=(n//36)
    s=((n-(36*t36))//6)
    unit=(n%6)
    list=[t36,s,unit]
    ndom=str(list[0]) + str(list[1]) + str(list[2])
    ndom=int(ndom)
    return ndom

def ndom_to_decimal(n):
    n =str(n)
    x = len(n)
    if x>1:
        s=6*eval(n[-2])
    else:
        s=0
    if x>2:
        t36 = 36*eval(n[-3])
    else:
        t36=0
    unit=eval(n[-1])
    decimal =t36+s+unit
    return decimal

def ndom_add(x,y):
    x =ndom_to_decimal(x)
    y =ndom_to_decimal(y)
    result =x + y
    result =decimal_to_ndom(result)
    return result

def ndom_multiply(x,y):
    x=ndom_to_decimal(x)
    y=ndom_to_decimal(y)
    answer=x*y
    answer = decimal_to_ndom(answer)
    return answer

