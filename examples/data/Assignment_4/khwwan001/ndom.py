def decimal_to_ndom(a):
    b=a%36
    if a<36:
        d=a%6
        if a<6:
            return(a)
        else : return(eval(str(a//6)+str(d)))

    else:
        z=a//36
        if b<6:
            return(eval(str(z)+str(0)+str(b)))
        else:
            c=b//6
            return(eval(str(z)+str(c)+str(b%6)))

    
    
def ndom_to_decimal(a):
    b=str(a)
    if len(b)==3:
            decimal=eval(b[0])*36+eval(b[1])*6+eval(b[2])*1
            return(decimal)
    
    elif len(b)==2:                                                                
             decimal=eval(b[0])*6+eval(b[1])*1
             return(decimal)

    else:
        return(a)

def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=decimal_to_ndom(x+y)
    return z

def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=decimal_to_ndom(x*y)
    return z
