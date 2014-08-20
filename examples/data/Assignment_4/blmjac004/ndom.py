def ndom_to_decimal(a):
    dec=0
    exp=0
    num=a
    while (num!=0):
        dec+=num%10*6**exp
        num=num//10
        exp+=1
    return dec
    
def decimal_to_ndom(a):
    x=''
    while True:
        x=str(a%6)+x
        a=a//6
        if (a==0):
            break
    return x

    
    
def ndom_add(a,b):
    newa=ndom_to_decimal(a)
    newb=ndom_to_decimal(b)
    add=newa+newb
    return (decimal_to_ndom(add))
    

def ndom_multiply(a,b):
    new_a=ndom_to_decimal(a)
    new_b=ndom_to_decimal(b)
    times= new_a*new_b
    return (decimal_to_ndom(times))