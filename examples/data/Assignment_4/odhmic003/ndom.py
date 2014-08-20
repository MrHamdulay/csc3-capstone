def ndom_to_decimal(a):
    a= str(a)
    if len(a)==3:
        q= int(a[0])*36
        w= int(a[1])*6
        e= int(a[2])
        r= (q+w+e)
        return (r)
    elif len(a)==2:
        q= int(a[0])*6
        w= int(a[1])
        r= (q+w)
        return (r)
    elif len(a)==1:
        q= int(a[0]) 
        r= (q)
        return (r)


def decimal_to_ndom(a):
    f= a//36
    g= f*100
    h= a- (36*f)
    i= h//6
    l= i*10
    j= i*6
    k= h-j
    return (g+l+k)

    
def ndom_add(a,b):
    
    a= str(a)
    b= str(b)
    if len(a)==3:
        q= int(a[0])*36
        w= int(a[1])*6
        e= int(a[2])
        r= (q+w+e)
        
    elif len(a)==2:
        q= int(a[0])*6
        w= int(a[1])
        r= (q+w)
        
    elif len(a)==1:
        q= int(a[0]) 
        r= (q)
        

    
    if len(b)==3:
        z= int(b[0])*36
        x= int(b[1])*6
        c= int(b[2])
        t= (z+x+c)
        
    elif len(b)==2:
        x= int(b[0])*6
        c= int(b[1])
        t= (x+c)
        
    elif len(b)==1:
        c= int(b[0]) 
        t= (c)
          
    
    ans= (r)+(t)
    f= ans//36
    g= f*100
    h= ans- (36*f)
    i= h//6
    l= i*10
    j= i*6
    k= h-j
    return (g+l+k)    
    
    
    
def ndom_multiply(a,b):
    a= str(a)
    if len(a)==3:
        q= int(a[0])*36
        w= int(a[1])*6
        e= int(a[2])
        r= (q+w+e)
        
    if len(a)==2:
        q= int(a[0])*6
        w= int(a[1])
        r= (q+w)
        
    if len(a)==1:
        q= int(a[0])
        r= (q)
         
    b= str(b)
    
    if len(b)==3:
        z= int(b[0])*36
        x= int(b[1])*6
        c= int(b[2])
        t= (z+x+c)
        
    if len(b)==2:
        x= int(b[0])*6
        c= int(b[1])
        t= (c+x)
        
    if len(b)==1:
        c= int(b[0])
        t= (c)
               
    ans= (r)*(t)
    f= ans//36
    g= f*100
    h= ans- (36*f)
    i= h//6
    l= i*10
    j= i*6
    k= h-j
    return(g+l+k)    
    
    
    