def ndom_to_decimal(z):
    o=0
    ind=0
    z=str(z)
    for i in z[::-1]:
        o+=int(i)*(6**ind)
        ind+=1
    return(o)
    
def decimal_to_ndom(z):
    if z>=(6**3):
        o=""
        pow=3
        for i in range(4):
            spl=z//(6**pow)
            o+=str(spl)[0]
            z=z%(6**pow)
            pow-=1
        return(int(o))
    elif z>=(6**2):
        o=""
        pow=2
        for i in range(3):
            spl=z//(6**pow)
            o+=str(spl)[0]
            z=z%(6**pow)
            pow-=1
        return(int(o))
    elif z>=(6):
        o=""
        pow=1
        for i in range(2):
            spl=z//(6**pow)
            o+=str(spl)[0]
            z=z%(6**pow)
            pow-=1
        return(int(o))   
    else:
        return(z)

def ndom_add(m,n):
    w=ndom_to_decimal(m)
    t=ndom_to_decimal(n)
    r=w+t
    return(decimal_to_ndom(r))

def ndom_multiply(m,n):
    w=ndom_to_decimal(m)
    t=ndom_to_decimal(n)
    r=w*t
    return(decimal_to_ndom(r))

        
        
        