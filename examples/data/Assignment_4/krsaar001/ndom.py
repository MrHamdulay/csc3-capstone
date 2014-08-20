def ndom_to_decimal(a):
    a=str(a)
    units=eval(a[-1])
    tens=0
    hundereds=0
    
    if len(a)==3:
        tens=eval(a[-2])*6
        hundereds=eval(a[-3])*36
    if len(a)==2:
        tens=eval(a[-2])*6
        
    return(units+tens+hundereds)

    
def decimal_to_ndom(a):
    
    units=a%6
    tens=((a-units)%36)//6
    hundereds=(a-units-tens*6)//36
    
    if hundereds:
        return(str(hundereds)+str(tens)+str(units))
    elif tens:
        return(str(tens)+str(units))
    else:
        return(str(units))
    
def ndom_add(a,b):
    sumN=ndom_to_decimal(a)+ndom_to_decimal(b)
    return(decimal_to_ndom(sumN))
    
def ndom_multiply(a,b):
    product=ndom_to_decimal(a)*ndom_to_decimal(b)
    return(decimal_to_ndom(product))
    
