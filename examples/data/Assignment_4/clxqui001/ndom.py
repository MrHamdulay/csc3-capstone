def decimal_to_ndom(a):
    d=a//36
    e=(a%36)//6
    f=(a%36)%6
    if d==0:
        num=str(e)+str(f)
    elif d!=0:
        num=str(d)+str(e)+str(f)
    num1=int(num)
    return num1

def ndom_to_decimal(a):
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
   
    
    
            
            
    
    
    
