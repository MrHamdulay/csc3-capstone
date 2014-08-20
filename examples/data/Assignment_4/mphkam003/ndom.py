def ndom_to_decimal (a):
    b=str(a)
    c=b[::-1]
    A=0
    for i in range(len(b)):
        
        A+= int(c[i])*6**i
    
            
    return A

def decimal_to_ndom (a):         
    A=""
    if a//6**2!=0:
        for i in range(2,0-1,-1):
            A = A + str(a//(6**i))
            a = a%6**i
    elif a//6!=0:
        for i in range(1,0-1,-1):
                    A = A + str(a//(6**i))
                    a = a%6**i  
    else:
        for i in range(1):
                            A = A + str(a//(6**i))
                            a = a%6**i         
        
    return A
        
    
def ndom_add(a,b):
    j = ndom_to_decimal(a) + ndom_to_decimal(b)
    k = decimal_to_ndom(j)
    return k
        
def ndom_multiply(a,b):
    j = ndom_to_decimal(a) * ndom_to_decimal(b) 
    k = decimal_to_ndom(j)
    return k