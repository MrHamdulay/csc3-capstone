def ndom_to_decimal(a):
    q = str(a)
    w = len(q)
    e = 0
    r = (eval(str(a)[e]))
    if w == 3:
        t = (r*(6**(w-1))) + (eval(str(a)[1])*(6**(w-2))) + (eval(str(a)[2])*(6**(w-3)))
        return t
    elif w == 2:
        t = (r*(6**(w-1))) + (eval(str(a)[1])*(6**(w-2)))
        return t
    elif w == 1:
        t = (r*(6**(w-1)))
        return t
   

def decimal_to_ndom(a):
    c = str(a)
    h = len(c)
    g = 0
    if h == 3:
        k = a//6
        l= round(a%6)
        R = k//6
        j= round(k%6)
        f = R//6
        s = round(R%6)
        d = (s*100) + (j*10) + (l*1)
        return d
       
    elif h==2:
        k = a//6
        l= round(a%6)
        if l == 0:
            R = k//6
            j= round(k%6)
            f = R//6
            s = round(R%6)
            d = (s*100) + (j*10) + (l*1)
            return d
           
        else:
            R = k//6
            j= round(k%6)        
            d = (j*10) + (l*1)
            return d
            
        
    elif h== 1:
        k = a//6
        l= round(a%6)
        if l == 0:
            R = k//6
            j= round(k%6)        
            d = (j*10) + (l*1)
            return d

        else:
            d = (l*1)
            return d

        
def ndom_add(a,b):
    y= ndom_to_decimal(a)
    x = ndom_to_decimal(b)
    sumA = y + x
    z= decimal_to_ndom(sumA)
    return z

def ndom_multiply(a,b):
    y= ndom_to_decimal(a)
    x = ndom_to_decimal(b)
    sumA = y * x
    z= decimal_to_ndom(sumA)
    return z
