#RYXSHR002
#4/04/14
#ndom calculations


def ndom_to_decimal(a):
    k= str(a)
    p= 0
    
    for i in k[:len(k)-1]:
        
        p=p +int(i)
        p=p*6
        
    z= p +int(k[len(k)-1])
    return z

def decimal_to_ndom(a):
    
    k=''
    i=a
    while (i!=0):
        i= (a//6)
        k= (k+ str(a%6))
        a=i
        
    return str(k)[::-1] 

def ndom_add(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))

def ndom_multiply(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
                                    