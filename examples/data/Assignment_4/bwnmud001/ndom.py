def ndom_to_decimal(a):
    b=str(a)
    z=b[::-1]
    t=z[0]
    t=int(t)
    
    y=z[1:2]
    if y!="":
        y=(int(y))*6
    else: 
        y=0
        
    w=z[2:3]
    if w!="":
        w=(int(w))*36
    else: 
        w=0
    sum=t+w+y
    return(sum)

def decimal_to_ndom(a):
    if a>=36:
        n=a//36
        n_n=str(n)
        q=a%36
        w=a%6
        w=str(w) 
        e=q//6
        m=str(e)
        sm=(n_n+m+w)
        z=eval(sm)
        return(z) 
    else:
        q=a%36
        w=a%6
        w=str(w) 
        e=q//6
        m=str(e)
        sm=(m+w)
        z=eval(sm)
        return(z)


def ndom_add (a,b):
    aa=ndom_to_decimal(a)
    bb=ndom_to_decimal(b)
    sm=(aa)+(bb)
    e=decimal_to_ndom(sm)
    return(e)


def ndom_multiply(a,b):
    aa=ndom_to_decimal(a)
    bb=ndom_to_decimal(b)  
    w=aa*bb
    e=decimal_to_ndom(w)
    return(e)



    

