

def decimal_to_ndom(a):
    x =(a//36)
    y =((a-(36*x))//6)
    digits=(a%6)
    list=[x,y,digits]
    string=str(list[0]) + str(list[1]) + str(list[2])
    string=int(string)
    return string

def ndom_to_decimal(a):
    a=str(a)
    if len(a)>1:
        y =eval(a[-2])*6
    else:
        y=0
    if len(a)>2:
        x =eval(a[-3])*36
    else:
        x =0
    z=eval(a[-1])
    number=x+y+z
    return number

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    ans =a+b
    ans =decimal_to_ndom(ans)
    return ans

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    ans=a*b
    ans=decimal_to_ndom(ans)
    return ans

