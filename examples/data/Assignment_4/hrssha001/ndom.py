def ndom_to_decimal(a):
    a=str(a)
    if len(a)==3:
        x = a[2] 
        y = a[1] 
        z = a[0] 
        c = eval(x) + eval(y) * 6 + eval(z) * 36
        
    if len(a)==2:
        x = a[1] 
        y = a[0]  
        c = eval(x) + eval(y) *6
    
    if len(a)==1:
        c=eval(a[0])
    
    return c
    
    

def decimal_to_ndom(a):
    if a > 216:
        x=int(a)//6
        y=int(a)%6
        c=x//6
        d=x%6
        g=c//6
        h=c%6
        m=g//6
        n=g%6
        z=str(y)
        f=str(d)
        j=str(h)
        p=str(n)
        c=eval(p+j+f+z)
    if 36 <= a <= 216:
        x=int(a)//6
        y=int(a)%6
        c=x//6
        d=x%6
        g=c//6
        h=c%6
        z=str(y)
        f=str(d)
        j=str(h)
        c = eval(j+f+z)
    
    if 6 <= a < 36:
        x=int(a)//6
        y=int(a)%6
        c=x//6
        d=x%6
        z=str(y)
        f=str(d) 
        c=eval(f+z)
    if a <=5:
        c = a

    return c
 
def ndom_add(a,b):
    m = ndom_to_decimal(a)
    n = ndom_to_decimal(b)
    c = m + n
    x = decimal_to_ndom(c)
    return x
 
def ndom_multiply(a,b):
    m = ndom_to_decimal(a)
    n = ndom_to_decimal(b)        
    c = m*n
    x = decimal_to_ndom(c)
    return x


