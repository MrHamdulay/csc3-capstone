def ndom_to_decimal (num):
    if num<6:
        result=num
    elif 56>num>=10:
        n=num//10
        j=n*6
        m=num%10
        k=j+m
        result=k
    elif num>=100:
        n=num//100
        j=n*36
        m=num%100
        o=m//10
        p=o*6
        q=m%10
        r=j+p+q
        result=r
    return result
        
def decimal_to_ndom(num):
    if num<6:
        c=num%6
        result=c
    elif 6<=num<36:
        b=num//6
        c=num%6   
        result=str(b)+str(c)
    if num>=36:
        a=num//36
        d=num%36
        b=d//6
        c=d%6
        result=str(a)+str(b)+str(c)
    return result

def ndom_add (a,b):
    ansa=ndom_to_decimal(a)
    ansb=ndom_to_decimal(b)
    addans=ansa+ansb
    ansfinal=decimal_to_ndom(addans)
    return ansfinal

def ndom_multiply(a,b):
    ansa=ndom_to_decimal(a)
    ansb=ndom_to_decimal(b)
    multans=ansa*ansb
    ansfinal=decimal_to_ndom(multans)
    return ansfinal