def ndom_to_decimal(a):
    x=str(a)
    z=0
    for i in x[:len(x)-1]:
        z+=int(i)
        z*=6
    y= z +int(x[len(x)-1])
    return y
def decimal_to_ndom (a):
    x= ''
    i=a
    while i!=0:
        i=a//6
        x+=str(a%6)
        a=i
    return str(x) [::-1]
def ndom_add (a,b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
def ndom_multiply (a,b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))

    
            
                    
                
                    
            
                