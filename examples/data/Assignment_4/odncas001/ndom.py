def ndom_to_decimal(a):
    a=str(a)
    if len(a)==3:
        x=36*eval(a[0])+6*eval(a[1])+eval(a[2])
    if len(a)==2:
        x=6*eval(a[0])+eval(a[1])
    if len(a)==1:
        x=eval(a)
    return x

def decimal_to_ndom(a):
    if a//36:
        x1=a//36
        if (a%36)//6:
            x2=(a%36)//6
            if (a%36)%6:
                x3=(a%36)%6
            else:
                x3=0
        else:
            x2=0
            x3=a%36
    elif a//6:
        x1=0
        x2=a//6
        x3=a%6
    else:
        x1=0
        x2=0
        x3=a
    ans=str(x1)+str(x2)+str(x3)
    if a!=0:
        while ans[0]=="0":
            ans=ans[1:]
    return eval(ans)
        
def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a+b
    c=decimal_to_ndom(c)
    return c

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a*b
    c=decimal_to_ndom(c)
    return c    


                
            
        
    
        
    
