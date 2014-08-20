def ndom_to_decimal(a):
    dec=((a//100)*36)+(((a%100)//10)*6)+((a%100)%10)
    return dec

def decimal_to_ndom(a):
    ans=((a//36)*100)+((a%36//6)*10)+(a%36)%6
    return ans

def ndom_add(a,b):
    c=ndom_to_decimal(a)+ndom_to_decimal(b)
    ans=decimal_to_ndom(c)
    return ans

def ndom_multiply(a,b):
    c=ndom_to_decimal(a)*ndom_to_decimal(b)
    ans=decimal_to_ndom(c)
    return ans    