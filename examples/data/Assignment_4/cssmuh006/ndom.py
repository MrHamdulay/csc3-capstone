
import math

def decimal_to_ndom(a):
    
    dec=0
    m=a
    i=0
    
    while(m!=0):        
        
        dec+=m%6*10**i
        m=m//6
        i+=1
        
    return dec
    
    
def ndom_to_decimal(a):
    
    ndom=0
    s=str(a)
    l=len(s)
    
    for i in range(l):        
        
        ndom+=eval(s[i:i+1])
        
        if(i<l-1):
            ndom*=6
        
    return ndom
    
def ndom_add(a,b):
    
    s=0
    q=str(a+b)
    l=len(q)
    
    for i in range(l):

        d=eval(q[i:i+1])        
        
        if(d%6==0 and (i>=1)):      
            s+=(d//6)*10**(l-i)
            
        elif(d>6 and i>=1):
            s+=(d//6)*10**(l-i)
            s+=(d%6)*10**(l-(i+1))
           
        else:
            s+=d*10**(l-(i+1))
    q=str(s)
    d=eval(q[0:1])
    
    if(d>=6):
        s=d//6*1000+d%6*100+eval(q[1:])
    
    return s            
    
def ndom_multiply (a,b):
    
    q=ndom_to_decimal(a)
    p=ndom_to_decimal(b)
    
    prod=q*p
    prod=decimal_to_ndom(prod)
    
    return prod
    