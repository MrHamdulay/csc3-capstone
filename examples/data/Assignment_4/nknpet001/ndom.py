# My Ndom module
# peter nkuna
# 2 April 2014

def ndom_to_decimal (a):
    ans=0
    
    a=str(a)
    
    x=len(a)
    
    for i in a:
        x=x-1
        i=int(i)
        ans=ans+(i*(6**x))
        
    return(ans)
        
def decimal_to_ndom (a):
    quot=a
    
    ans=""
    
    while quot !=0:
        r = quot%6
        quot =quot//6
        r=str(r)
        ans+=r
       
    return(ans[::-1])    

def ndom_add (a,b):
    sola=0
    
    a=str(a)
    e=len(a)
    for i in a:
        e=e-1
        i=int(i)
        sola +=(i*(6**e))
            
    solb=0
    b=str(b)
    e=len(b)
    for i in b:
        e=e-1
        i=int(i)
        solb +=(i*(6**e))
        
    sol = sola +solb
       
    q = sol
    na=""
    while q !=0:
        r = q%6
        q =q//6
        r=str(r)
        na+=r
    return(na[::-1])

def ndom_multiply (a, b):
    
    sola=0
    a=str(a)
    e=len(a)
    for i in a:
        e=e-1
        i=int(i)
        sola =sola+(i*(6**e))
            
    solb=0
    b=str(b)
    e=len(b)
    for i in b:
        e=e-1
        i=int(i)
        solb =solb+(i*(6**e))
        
    sol = sola *solb
       
    q=sol
    na=""
    while q !=0:
        remainder = q%6
        q = q//6
        r=str(q)
        na+=r
    return(na[::-1])        