def ndom_to_decimal(a):
    sum=0
    new=0
    for i in str(a):
        sum=new*6
        new=sum+eval(i)
    return(new)
    #print(new)
    
#ndom_to_decimal(1524)
    
    
    
    
def decimal_to_ndom(a):
    x=0
    sum=0
    while a!=0:
        b=(a%6)*(10**(x))
        a=a//6
        sum=sum+b
        x+=1
    return(sum)
        
#decimal_to_ndom(12)  


def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x+y
    j=decimal_to_ndom(z)
    #print(j)
    return(j)
    
#ndom_add(123,141)
    
def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x*y
    j=decimal_to_ndom(z)
    #print(j)
    return(j)    

#ndom_mutiply(13,14)