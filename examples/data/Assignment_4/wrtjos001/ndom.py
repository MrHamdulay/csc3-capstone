def ndom_to_decimal(a):
    x=a%100
    y=x%10
    ans=((a//100)*36) + ((x//10)*6)+y
    return ans

def decimal_to_ndom(a):
    x=a%36
    y=x%6
    ans=((a//36)*100)+((x//6)*10)+y
    return ans

def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x+y
    ans=decimal_to_ndom(z)
    return ans

def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x*y
    ans=decimal_to_ndom(z)
    return ans
