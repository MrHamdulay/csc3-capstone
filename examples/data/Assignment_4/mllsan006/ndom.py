def ndom_to_decimal(a):
    c=a%100
    d=c%10
    ans=((a//100)*36)+((c//10)*6)+d
    return ans

def decimal_to_ndom(a):
    c=a%36
    d=c%6
    ans=((a//36)*100)+((c//6)*10)+d
    return ans
    
def ndom_add(a, b):
    z=ndom_to_decimal(a)
    c=ndom_to_decimal(b)
    d=z+c
    ans=decimal_to_ndom(d)
    return ans

def ndom_multiply(a, b):
    z=ndom_to_decimal(a)
    c=ndom_to_decimal(b)
    d=z*c
    ans=decimal_to_ndom(d)
    return ans