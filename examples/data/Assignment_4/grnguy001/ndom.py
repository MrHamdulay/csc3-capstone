#Base 6 
def ndom_to_decimal(a):
    total=0
    n=0    
    a=str(a)
    a=a[::-1]
    for i in range(len(a)):        
        j=int(a[n])*6**i
        total+=j
        n+=1
    return(total)


def decimal_to_ndom (a):
    y=a%6
    x=a//6
    b=""
    while x!=0 :
        if y==0:
            b+=str(a%6)
        else:
            b+=str(y)
        
        if x!=0:
            a=a//6
            y=a%6
            x=x//6
        else:
            break
    b+=str(a)
    b=b[::-1]
    b=int(b)
    return(b)
    
def ndom_add(a,b):
    c=ndom_to_decimal(a)+ndom_to_decimal(b)
    c=decimal_to_ndom(c)
    return(c)

def ndom_multiply(a,b):
    c=ndom_to_decimal(a)*ndom_to_decimal(b)
    c=decimal_to_ndom(c)
    return(c)