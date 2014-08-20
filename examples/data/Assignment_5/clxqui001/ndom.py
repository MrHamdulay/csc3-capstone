def ndom_to_decimal(a):
    f=a//36
    if f/36<1:
        f=""
    b=a//6
    if b==0:
        b=""
    c=a%6
    return a+b+c
    
def decimal_to_ndom(a):
    if len(str(a))==3:
        a=int(str(a)[0])*36+int(str(a)[1])*6+int(str(a)[2])
        return a
        
    elif len(str(a))==2:
        a=int(str(a)[0])*6+int(str(a)[1])
        return a
        
    elif len(str(a))==1:
        return a
        
def ndom_add(a,b):
    x=ndom_to_decimal(a)
    c=ndom_to_decimal(b)
    p=x+c
    d=decimal_to_ndom(p)
    return d
    
def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    c=ndom_to_decimal(b)
    p=x*c
    d=decimal_to_ndom(p) 
    return d
    
   
    
    
            
            
    
    
    
