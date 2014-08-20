def decimal_to_ndom(a):
    d="" 
    while a != 0:
        b=a//6
        c=a-(b*6)
        a=b
        d = d + str(c)
    e=d[::-1] 
    f=eval(e)
    return f

def ndom_to_decimal(w):
    g=str(w)
    h=-len(g)
    j=-1
    l=0
    while j>h:
        for k in range (len(g)):
            m=int(g[j])*(6**k)
            l+=m
            j-=1  
    return l
    #print (l)
    
def ndom_add(q,r):
    q2=ndom_to_decimal(q)
    r2=ndom_to_decimal(r)
    s=q2+r2
    s1=decimal_to_ndom(s)
    return s1

def ndom_multiply(q1,r1):
    q1=ndom_to_decimal(q1)
    r1=ndom_to_decimal(r1)
    s1=q1*r1
    s1=decimal_to_ndom(s1)
    
    return s1


    

