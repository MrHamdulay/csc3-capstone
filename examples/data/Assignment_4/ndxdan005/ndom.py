def decimal_to_ndom(n):
    
    x=0
    y=1
    
    while n//6>0:
                
        x+=(n%6)*y
        n=n//6
        y=y*10        
    
    x+=(n%6)*y
    
    return x


def ndom_to_decimal(n):
    
    n=str(n)
    y=len(n)
    
    if y==3:
        
        a=eval(n[0])
        b=eval(n[1])
        c=eval(n[2])
        
        x=a*36+b*6+c
        
    elif y==2:
        
        a=eval(n[0])
        b=eval(n[1])
        
        x=a*6+b
        
    elif y==1:
        
        a=eval(n[0])
        
        x=a
        
    return x

        
def ndom_add(a,b):
    
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    
    decimal=x+y
    
    ndom=decimal_to_ndom(decimal)
    
    return ndom


def ndom_multiply(a,b):
    
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    
    decimal=x*y
    
    ndom=decimal_to_ndom(decimal)
    
    return ndom