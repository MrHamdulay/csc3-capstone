def ndom_to_decimal(a):
    ndom = str(a)
    num = 0
    
    if len(ndom) == 3 :
        fir = int(ndom[0])
        sec = int(ndom[1])
        thi = int(ndom[2])
        
        fir = fir * 36
        sec = sec * 6
        thi = thi * 1
        
        num = fir + sec + thi
        
    elif len(ndom) == 2 :
        fir = int(ndom[0])
        sec = int(ndom[1])  
        
        fir = fir *6
        sec = sec * 1
        
        num = fir + sec
        
    elif len(ndom) == 1 :
        num = int(ndom)
    
    return num
    
def decimal_to_ndom(a):
    dec = str(a)
    div = 0
    rem = 0
    num = ''
    output = 0
    
    if len(dec) == 3 :
        div = int(dec) // 36
        rem = int(dec) % 36
        num += str(div)
        
        div = rem // 6
        rem = rem % 6
        num += str(div) + str(rem)
        
        output = int(num)
       
    elif len(dec) == 2 :
        div = int(dec) // 36
        rem = int(dec) % 36
        num += str(div)
        
        div = rem // 6
        rem = rem % 6
        num += str(div) + str(rem)
        
        output = int(num)
        
    elif len(dec) == 1 :
        div = int(dec) // 36
        rem = int(dec) % 36
        num += str(div)
        
        div = rem // 6
        rem = rem % 6
        num += str(div) + str(rem)
        
        output = int(num)        
        
        output = int(num)
        
    return output
    
def ndom_add (a, b):
    numF = 0
    numS = 0
    out = 0
    output = 0
    
    numF = ndom_to_decimal(a)
    numS = ndom_to_decimal(b)
    
    out = numF + numS
    
    output = decimal_to_ndom(out)
    
    return output

def ndom_multiply (a, b):
    numF = 0
    numS = 0
    out = 0
    output = 0
    
    numF = ndom_to_decimal(a)
    numS = ndom_to_decimal(b)
    
    out = numF * numS
    
    output = decimal_to_ndom(out)
    
    return output