def ndom_to_decimal(a):
    """converts a Ndom number to decimal"""
    num1=(a%10)
    num2=((a-num1)%100)//10*6
    num3=(a-(a%100))//100*36 
    dec=num1+num2+num3
    return dec
def decimal_to_ndom (a):
    """converts a decimal number to Ndom"""
    ndo=""    
    num=a//6
    rem=a%6
    ndo=ndo+str(rem)
    num2=num//6
    rem=num%6
    ndo=ndo+str(rem)   
    num3=num2//6
    rem=num2%6
    ndo=ndo+str(rem)
    ndo= ndo[::-1]
    if(ndo[0]=='0'):
        if(ndo[1]=='0'):
            ndom=ndo[2]
        else:
            ndom=ndo[1:]
    else:
        ndom=ndo
    return ndom
def ndom_add (a, b):
    """adds 2 Ndom numbers"""
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    add=x+y
    sumab=decimal_to_ndom(add)
    return sumab
def ndom_multiply (a, b):
    """multiples 2 Ndom numbers"""
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    multi=x*y
    mab=decimal_to_ndom(multi)
    return mab
