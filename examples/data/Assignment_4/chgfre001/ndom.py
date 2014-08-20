#program to convert numbers into Ndom* language
#by Frederick Chigwaza
#4 April 2014

def ndom_to_decimal(a):
    n=a
    d=0 
    e=0
    
    while n!=0:
        
        d=d+(n%10)*(6**e)
        n=n//10
        
        e+=1
    return d    
    
        


def decimal_to_ndom(a):
    n=a
    d=0
    e=0
    
    while n!=0:
        d+=(n%6)*(10**e)
        n=n//6
        e+=1
    return d
    


def ndom_add(a,b):
    
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    x=a+b
    
    x=decimal_to_ndom(x)
    return x


def ndom_multiply(a,b):
    
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    x=a*b
    
    c=decimal_to_ndom(x)
    
    return c
    
        
    
    
    