def ndom_to_decimal(a):
    z=str(a)
    if len(z)==3:
        n = int(z[0:1])*36+int(z[1:2])*6+int(z[2:3])
    elif len(z)==2:
        n = int(z[0:1])*6+int(z[1:2])
    else:
        n = int(z[0:1])
    return(n)

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
    ans=decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
    return(ans)
    
    
def ndom_multiply(a,b):
    result=decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
    return(result)    
