#ndom_to_decimal (a), that converts a Ndom number to decimal
#ecimal_to_ndom (a), that converts a decimal number to Ndom
#dom_add (a, b), that adds 2 Ndom numbers
#ndom_multiply (a, b), that multiples 2 Ndom numbers


def ndom_to_decimal (a):
    first=a%10
    second=((a%100-a%10)*6)//10
    third=(((a%1000-a%100)*36)//100)
    dec = first+second+third
    return dec


def decimal_to_ndom (a):
    third=(a//36)*100
    second=((a%36)//6)*10
    first=a%6
    ndom=third+second+first
    return ndom
def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a+b
    c=decimal_to_ndom(c)
    return c

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a*b
    c=decimal_to_ndom(c)
    return c    
    


    

