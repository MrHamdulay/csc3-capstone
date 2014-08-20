
#Programme ndom
#Shivaan Motilal
#4 April 2014


def decimal_to_ndom(a):
    """Continually divide by 6"""
    decimal=a
    denom=6
    ndom=""
    
    while True:
        if decimal>=6:
            ndom+=str(decimal%denom)
            decimal =decimal//denom
            
        
        else: 
            ndom +=str(decimal)
            ndom=ndom[::-1]                                      #reversing 
            break
            
            
    return ndom

def ndom_to_decimal(a):
    a=str(a)
    ndom=a[::-1]
    decimal=0
    power=0
    
    for r in ndom:
        r=int(r)
        decimal+=r*(6**power)
        power+=1
        
    return decimal

def ndom_add(a,b):
    number=ndom_to_decimal(a)+ndom_to_decimal(b)

    number=decimal_to_ndom(number)
    return number


def ndom_multiply(a,b):
    number=ndom_to_decimal(a)*ndom_to_decimal(b)
    number=decimal_to_ndom(number)
    return number
    
        
        
        
        
        
    
    
    




    
            
            
    

        
    
    
    




    