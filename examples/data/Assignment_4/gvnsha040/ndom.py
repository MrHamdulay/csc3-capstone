def decimal_to_ndom (a):
    

    a=str(a)

    if len(a) == 1:
        b=eval(a)
        b=b%6
        f=(b)
        return(f)
    
    elif len(a) == 2:
        c=eval(a)
        c_one=c%6
        #print(c_one)
        
        d=c//6
        d_one=d%6
        #print(d_one)
        #print(d_one,c_one, sep='')
        
        e=d//6
        #print(e)
        e_one=e%6
        if e_one == 0:
            f=(str(d_one)+str(c_one))
            return(f)
        
        else:
            
            f=(str(e_one)+str(d_one)+str(c_one))
            return(f)
        
    elif len(a) == 3:
        c=eval(a)
        c_one=c%6
        #print(c_one)
        
        d=c//6
        d_one=d%6
        #print(d_one)
        #print(d_one,c_one, sep='')
        
        e=d//6
        #print(e)
        e_one=e%6
        #print(e_one)
        #print(e_one,d_one,c_one, sep='')
        
        
        f_one=e//6
        if f_one == 0:
            f=(str(e_one)+str(d_one)+str(c_one))
            return(f)
            
        else:
            f=(str(f_one)+str(e_one)+str(d_one)+str(c_one))
            return(f)
        
        
        
        
        
        
        
        
        
        
        
def ndom_to_decimal (a):
                


        
                a = str(a)
        
                if len(a) == 1:
                            
                                b=a[0:1]
                                b=eval(a)
                                f=(b)
                                return(f)
                
                elif len(a) == 2:
                                
                                c=a[0:1]
                                #print(c)
                                c=eval(c)
                                c= c*6
                                #print(c)
                                
                                
                                d=a[1:2]
                                d=eval(d)
                                d=c+d
                                f=(d)
                                return(f)
                                
                                
                elif len(a) == 3:
                                
                                c=a[0:1]
                                #print(c)
                                c=eval(c)
                                c= c*6
                                #print(c)
                
                                
                                d=a[1:2]
                                d=eval(d)
                                d=c+d
                                d=d*6
                                #print(d)
                                
                                e=a[2:3]
                                e=eval(e)
                                e=d+e
                                f=(e)
                                return(f)
                            
                            
                            
                            
                            
                            
                            
                            
def ndom_add (a,b):
    
    c=ndom_to_decimal(a)
    d=ndom_to_decimal(b)
    
    x=c+d
    
    y=decimal_to_ndom(x)
    
    return(y)
    
    
    
def ndom_multiply (a, b):
    
    
    c=ndom_to_decimal(a)
    d=ndom_to_decimal(b)
    
    x=c*d
        
    y=decimal_to_ndom(x)
    
    return(y)
    