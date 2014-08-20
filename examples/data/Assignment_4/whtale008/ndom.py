def ndom_to_decimal(a):
    h= a//100
    t= (a//10)%10
    u = a%10
    
    n= ((((h*6)+t)*6)+u)
    return n

def decimal_to_ndom(a):
    qout = a
    n=0
    count=0
    while(qout != 0):
        n= n + (qout%6)*(10**count)
        qout = qout//6
        count = count +1
    
    return n

def ndom_add(a,b):
    n = ndom_to_decimal(a)+ndom_to_decimal(b)
    n= decimal_to_ndom(n)
    return n

def ndom_multiply(a,b):
    n = ndom_to_decimal(a)*ndom_to_decimal(b)
    n= decimal_to_ndom(n)
    return n    
    
        
    