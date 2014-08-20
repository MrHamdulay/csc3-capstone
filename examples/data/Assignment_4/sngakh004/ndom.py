def ndom_to_decimal(b):
    o=0
    ind=0
    b=str(b)
    for i in b[::-1]:
        o+=int(i)*(6**ind)
        ind+=1
    return(o)
    
def decimal_to_ndom(b):
    if b>=(6**3):
        o=""
        pow=3
        for i in range(4):
            spl=b//(6**pow)
            o+=str(spl)[0]
            b=b%(6**pow)
            pow-=1
        return(int(o))
    elif b>=(6**2):
        o=""
        pow=2
        for i in range(3):
            spl=b//(6**pow)
            o+=str(spl)[0]
            b=b%(6**pow)
            pow-=1
        return(int(o))
    elif b>=(6):
        o=""
        pow=1
        for i in range(2):
            spl=b//(6**pow)
            o+=str(spl)[0]
            b=b%(6**pow)
            pow-=1
        return(int(o))   
    else:
        return(b)

def ndom_add(c,d):
    w=ndom_to_decimal(c)
    t=ndom_to_decimal(d)
    r=w+t
    return(decimal_to_ndom(r))

def ndom_multiply(c,d):
    w=ndom_to_decimal(c)
    t=ndom_to_decimal(d)
    r=w*t
    return(decimal_to_ndom(r))

        
        
        