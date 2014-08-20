def ndom_to_decimal(intx):
    sm = 0
    x = str(intx)
    y = x[::-1]
    if len(y)==1:
        a = y[0]
        ai = (int(a))*1
        sm = ai
    if len(y)==2:
        a = y[0]
        b = y[1]
        ai = (int(a))*1
        bi = (int(b))*6
        sm = ai + bi       
    if len(y)==3:
        a = y[0]
        b = y[1]
        c = y[2]
        ai = (int(a))*1
        bi = (int(b))*6
        ci = (int(c))*36
        sm = ai + bi + ci      
    return sm
    
def decimal_to_ndom(intx):
    a = int(intx/36)
    b = int((intx%36)/6)
    c = int((intx%36)%6)
    sm = str(a)+str(b)+str(c)
    sm = int(sm)
    return sm
    
    
def ndom_add(intx,inty):
    sm = 0
    x = ndom_to_decimal(intx)
    y = ndom_to_decimal(inty)
    sm = x + y
    ret = decimal_to_ndom(sm)
    return(ret)
    

def ndom_multiply(intx,inty):
    sm = 0
    x = ndom_to_decimal(intx)
    y = ndom_to_decimal(inty)
    sm = x * y
    ret = decimal_to_ndom(sm)
    return(ret)    
    
       
    """sum = ""
    
    a = int(intx/36)
    print(a)
    b = int((intx%36)/6)
    print(b)
    c = int((intx%36)%6)
    print(c)
    
    if a == 0:
        a = ""
    if a == 0 and b == 0:
        a = ""
        b = ""
    
    sum = str(a) + str(b) + str(c)
    return sum"""
    




    """    if intx>99:              #3 digit
            a = str(intx)[0]
            b = str(intx)[1]
            c = str(intx)[2]
            sum = (int(a)*36) + (int(b)*6) + (int(c)*1)
            
        if 100>intx>9:           #2 digit
            a = str(intx)[0]
            b = str(intx)[1]  
            sum = (int(a)*6) + (int(b)*1) 
           
        if  10>intx>-1:           #1 digit
            a = str(intx)[0]
            sum = (int(a)*6) 
            
        return sum"""