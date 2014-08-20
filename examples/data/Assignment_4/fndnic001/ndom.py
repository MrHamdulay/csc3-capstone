def ndom_to_decimal(a):
    a=str(a)[::-1]
    l=len(a)
    p=1
    sum1=0
    for i in a:
        x=eval(i)*p
        p*=6
        sum1=sum1+x
    return sum1
    

def decimal_to_ndom(a):    
    x=a%6
    x=str(x)        
    y=(a//6)%6
    y=str(y)        
    z=(a//36)%6
    z=str(z)
    ans=z+y+x
    if ans[0]=='0':
        if ans[1]=='0':
            return ans[2:3]
        else: return ans[1:3]
    else:
        return ans
    
    
    
    
def ndom_add(a,b):   
    ans=ndom_to_decimal(a)+ndom_to_decimal(b)
    n=decimal_to_ndom(ans)
    return n

def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)    
    ans=x*y
    n=decimal_to_ndom(ans)
    return n   
   
       
    
    
    
    
    