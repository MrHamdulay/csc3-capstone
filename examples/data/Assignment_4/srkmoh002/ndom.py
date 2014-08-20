# question2

def ndom_to_decimal(a): 
    d=a
    decimal=0
    i=0
    while d!=0:
        decimal=decimal+((d%10)*(6**i))
        i=i+1
        d=d//10 
    decimal=int(decimal) 
    return decimal 
    
def decimal_to_ndom(a): 
    d=a
    ndom=0
    i=0
    while d!=0:
        ndom=ndom+((d%6)*(10**i))
        i=i+1
        d=d//6 
    ndom=int(ndom) 
    return ndom

def ndom_add(a,b):
    d1=a
    decimal=0
    i=0
    while d1!=0:
        decimal=decimal+((d1%10)*(6**i))
        i=i+1
        d1=d1//10 
    decimal1=int(decimal)
    
    d2=b
    decimal=0
    i=0
    while d2!=0:
        decimal=decimal+((d2%10)*(6**i))
        i=i+1
        d2=d2//10 
    decimal2=int(decimal)    
    
    decimal3=decimal1+decimal2
     
    d=decimal3
    ndom=0
    i=0
    while d!=0:
        ndom=ndom+((d%6)*(10**i))
        i=i+1
        d=d//6 
    ndom=int(ndom) 
    return ndom    

def ndom_multiply(a,b):
    d1=a
    decimal=0
    i=0
    while d1!=0:
        decimal=decimal+((d1%10)*(6**i))
        i=i+1
        d1=d1//10 
    decimal1=int(decimal)
    
    d2=b
    decimal=0
    i=0
    while d2!=0:
        decimal=decimal+((d2%10)*(6**i))
        i=i+1
        d2=d2//10 
    decimal2=int(decimal)    
    
    decimal3=(decimal1)*(decimal2)
     
    d=decimal3
    ndom=0
    i=0
    while d!=0:
        ndom=ndom+((d%6)*(10**i))
        i=i+1
        d=d//6 
    ndom=int(ndom) 
    return ndom    
            