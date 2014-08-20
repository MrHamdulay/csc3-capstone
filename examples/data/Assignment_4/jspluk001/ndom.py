#Luke Joseph
#1 April 2014
#question2 assignment4
def ndom_to_decimal2(a):
    A = str(a)
    t = len(A)
    p = 0
    x = (eval(str(a)[p]))
    if t == 3:
        y = (x*(6**(t-1))) + (eval(str(a)[1])*(6**(t-2))) + (eval(str(a)[2])*(6**(t-3)))
        print(y)
        
    elif t == 2:
        y = (x*(6**(t-1))) + (eval(str(a)[1])*(6**(t-2)))
        print(y)
        
    elif t == 1:
        y = (x*(6**(t-1)))
        print(y)
        
    
def ndom_to_decimal(a):
    A = str(a)
    t = len(A)
    p = 0
    x = (eval(str(a)[p]))
    if t == 3:
        y = (x*(6**(t-1))) + (eval(str(a)[1])*(6**(t-2))) + (eval(str(a)[2])*(6**(t-3)))
        return y
    elif t == 2:
        y = (x*(6**(t-1))) + (eval(str(a)[1])*(6**(t-2)))
        return y
    elif t == 1:
        y = (x*(6**(t-1)))
        return y
   

def decimal_to_ndom(a):
    A = str(a)
    t = len(A)
    p = 0
    if t == 3:
        y = a//6
        q= round(a%6)
        r = y//6
        o= round(y%6)
        b = r//6
        m = round(r%6)
        #v = str(m) + str(o) +str(q)
        v = (m*100) + (o*10) + (q*1)
        return v
       
    elif t==2:
        y = a//6
        q= round(a%6)
        if q == 0:
            r = y//6
            o= round(y%6)
            b = r//6
            m = round(r%6)
            #v = str(m) + str(o) +str(q)
            v = (m*100) + (o*10) + (q*1)
            return v
           
        else:
            r = y//6
            o= round(y%6)        
            v = (o*10) + (q*1)
            return v
            
        
    elif t== 1:
        y = a//6
        q= round(a%6)
        if q == 0:
            r = y//6
            o= round(y%6)        
            v = (o*10) + (q*1)
            return v

        else:
            v = (q*1)
            return v

        
def ndom_add(a,b):
    y= ndom_to_decimal(a)
    x = ndom_to_decimal(b)
    sumX = y + x
    s= decimal_to_ndom(sumX)
    return s

def ndom_multiply(a,b):
    y= ndom_to_decimal(a)
    x = ndom_to_decimal(b)
    sumX = y * x
    s= decimal_to_ndom(sumX)
    return s
    #print(sumX)

decimal_to_ndom(6)