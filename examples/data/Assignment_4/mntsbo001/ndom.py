def decimal_to_ndom(n):
    x=n//36
    y=(n-(36*x))//6
    digits=(n%6)
    list=[x,y,digits]
    string=str(list[0])+str(list[1])+str(list[2])
    string=int(string)
    return string 

def ndom_to_decimal(d):
    d=str(d)
    if len(d)>1:
        y =eval(d[-2])*6
    else:
        y=0
    if len(d)>2:
        x =eval(d[-3])*36
    else:
        x =0
    z=eval(d[-1])
    number=x+y+z
    return number    


def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    sumndom=a+b
    sumndom=decimal_to_ndom(sumndom)
    return sumndom

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    prdct=a*b
    prdct=decimal_to_ndom(prdct)
    return prdct
    
#Sbonelo Mntungwa
#MNTSBO001
#Finding base 6
#4 April 2014
    
    
    