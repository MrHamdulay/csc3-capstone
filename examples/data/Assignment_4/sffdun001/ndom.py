def ndom_to_decimal (a):  
    a=str(a)
    if len(a)==3:
        decimal=(36*eval(a[-3]))+(6*eval(a[-2]))+eval(a[-1])
    elif len(a)==2:
        decimal=6*eval(a[-2])+eval(a[-1])
    elif len(a)==1:
        decimal=eval(a)
    return decimal 
        
        
def decimal_to_ndom (a):    
    if (a/6)<1:
        ndom=a
    elif 1<=(a/6)<6:
        #might be a mistake with rounding
        ndom=((a//6)*10)+(a%6)
    elif 6<=(a//6):
        ndom=((a//36)*100)+((a%36)//6)*10+(a%36)%6
    return ndom
        
    
    
def ndom_add (a, b):
    dec_a=ndom_to_decimal (a)
    dec_b=ndom_to_decimal (b)
    summ=dec_a+dec_b
    new=decimal_to_ndom (summ)
    return new 
    
def ndom_multiply (a, b):
    dec_a=ndom_to_decimal (a)
    dec_b=ndom_to_decimal (b)
    product=dec_a*dec_b
    new=decimal_to_ndom (product)
    return new     
    

    

    
    