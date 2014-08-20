
def decimal_to_ndom(a):
    
    daffodil=(a//36)
    lily=((a-(36*daffodil))//6)
    rose=(a%6)
    list=[daffodil,lily,rose]
    string=str(list[0]) + str(list[1]) + str(list[2])
    string=int(string)
    return string

def ndom_to_decimal(a):
    a=str(a)
    if len(a)>1:
        lily=eval(a[-2])*6
    else:
        lily=0
    if len(a)>2:
        daffodil=eval(a[-3])*36
    else:
        daffodil=0
    rose=eval(a[-1])
    num=daffodil+lily+rose
    return num

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    ans=a+b
    ans=decimal_to_ndom(ans)
    return ans

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    ans=a*b
    ans=decimal_to_ndom(ans)
    return ans

