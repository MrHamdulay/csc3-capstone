def ndom_to_decimal(a):
    x=str(a)
    if len(x)==3:
        dec = int(x[0:1])*36+int(x[1:2])*6+int(x[2:3])
    elif len(x)==2:
        dec = int(x[0:1])*6+int(x[1:2])
    else:
        dec = int(x[0:1])
    return(dec)

def decimal_to_ndom(a):
    x = a//36
    y = (a%36)//6
    z = a-(x*36+y*6)
    x,y,z=str(x),str(y),str(z)
    if(x)=="0":
        x=""
    n = int(x+y+z)
    return(n)  

def ndom_add(a,b):
    answer=decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
    return(answer)
    
    
def ndom_multiply(a,b):
    answer=decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
    return(answer)    
