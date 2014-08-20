
import math



def ndom_to_decimal (a):
    a = str(a)
    m = 6**(len(a)-1)
    d = 0
    for i in a:
        y = eval(i)
        y = y * m
        i = eval(i)
        d+=y
        m//=6
        
    return d 






def decimal_to_ndom (a):
    power = (math.log(a))/(math.log(6))
    power = int(power)
    nodigits = power + 1
    divisor = 6**(power)
    
    ndom=""
    x=a

    for i in range(nodigits):
        y= x%divisor
        digit = (x-y)//divisor
        digit = str(digit)
        ndom+=digit
        x = y
        divisor//=6
    
    ndom=eval(ndom)        
    return ndom
                


    
    
def ndom_add (a, b):
    z =  ndom_to_decimal(a) + ndom_to_decimal(b)
    y = decimal_to_ndom(z)
    return y


def ndom_multiply (a, b):
    z = (ndom_to_decimal(a)) * (ndom_to_decimal(b))
    y = decimal_to_ndom(z)
    return y
   
    
    
    
    

             
    
        
        
        
    
    
    

    
    
        
    