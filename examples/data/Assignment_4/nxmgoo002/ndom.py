def decimal_to_ndom(num):
    if num >= 36:
        x = num % 36
        y = num // 36
        z = x % 6
        w = (num-y*36)//6
        t = (num-y*36)%6
        y,w,t = str(y), str(w), str(t)
        num = y+w+t
        num = int(num)


    elif num <36 and num >= 0:
        x = num % 6
        y = num // 6
        z = x % 1
        w = x // 1
        y,w, = str(y), str(w)
        num = y+w
        num = int(num)
    return num


def ndom_to_decimal(num):
    num=str(num)
    if len(num)==3:
        decimal=int(num[0])*36 + int(num[-2])*6 + int(num[-1])
    elif len(num)==2:
        decimal=int(num[0])*6 + int(num[1])
    elif len(num)==1:
        decimal=int(num)
    return decimal

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    num= a+b
    num=decimal_to_ndom(num)
    return num


def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    num= a*b
    num=decimal_to_ndom(num)
    return num




