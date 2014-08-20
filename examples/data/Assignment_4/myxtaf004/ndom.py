def ndom_to_decimal (a):
    a=str(a)
    a=a[-1::-1]
    x=0
    n=0
    for i in a:
        x+=int(i)*(6**n)     
        n+=1
    return x
    
def decimal_to_ndom (a):
    n=0
    x=0
    while x<a:
        n+=1
        x=6**n
        b=""
    c=a
    for i in range(n-1, -1, -1):
        x=0
        t=0
      
        while True:
            x=t*(6**i)
            if x>c:
                if t-1>-1:
                    t-=1
                c=c-t*(6**i)
                break
            t+=1
        b=b+str(t)
    return int(b)

def ndom_add (a, b):
    c=ndom_to_decimal (a)+ndom_to_decimal (b)
    return decimal_to_ndom (c)
        
def ndom_multiply (a, b):
    c=ndom_to_decimal (a)*ndom_to_decimal (b)
    return decimal_to_ndom (c)    