# ndom.py
# Wongwa Giqwa
# 02 April 2014

def ndom_to_decimal(a):
    b=str(a)
    c=0
    t=0
    x=0
    f=len(b)
    k=2
    if f==3:
        for i in range(f):
            j=b[c]
            d=int(j)*6**k
            x+=d
            c+=1
            k-=1
         #return (x)    
    elif f==2:
        for i in range(1,-1,-1):
            j=b[c]
            d=int(j)*6**i
            x+=(d)
            c+=1
        #return (x)
    #else:
        #print(a)
    return(x)
#ndom_to_decimal(123)
    #c=a%6
    #q=c*(1)
    #d=b//6
    #e=b%6
    #r=e*(6)
    #f=d%6
    #s=f*(6*6)
    #if f==0:
     #   print(r+q)
    #else:
     #   print(s+r+q)
#ndom_to_decimal(12)
        
    
        
def decimal_to_ndom(a): 
    b=a//6
    c=a%6
    d=b//6
    e=b%6
    f=d%6
    z=''
    if f==0:
        q=str(c)
        r=str(e)
        z+=r+q
    
        
    else:
        q=str(c)
        r=str(e)
        s=str(f)
        z+=s+r+q
    return (int(z))
#decimal_to_ndom(12)

def ndom_add(a,b):
    import ndom
    c=ndom.ndom_to_decimal(a)
    d=ndom.ndom_to_decimal(b)
    sum = c+d
    final = ndom.decimal_to_ndom(sum)
    return final
    #print(final)
    
#ndom_add(123,141)

def ndom_multiply(a,b):
    import ndom
    x=ndom.ndom_to_decimal(a)
    y=ndom.ndom_to_decimal(b)
    t = x*y
    f = ndom.decimal_to_ndom(t)
    return (f)
#ndom_multiply(13,14)
    
    
  
        
    
    
    
    
    

        
    
    
        
        
        

    
    


    
    
