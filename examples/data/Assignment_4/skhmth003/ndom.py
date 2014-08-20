def ndom_to_decimal(a):
    b=str(a)
    if len(b)>=3:
        c=b[2]
        d=b[1]
        e=b[0]
        f=int(c)*1
        g=int(d)*6
        h=int(e)*12
        i=f+g+h        
    elif len(b):
        d=b[1]
        e=b[0]
        g=int(d)*1
        h=int(e)*6
        i=g+h        
    else: 
        e=b[0]
        h=int(e)*1
        i=h
    return i
def decimal_to_ndom(a):
    b=a//6
    c=b//6
    d=c//6
    e=d//6
    #remainders
    f=str(a%6)
    g=str(b%6)
    h=str(c%6)
    i=str(d%6)
    j=i+h+g+f
    k=int(j)
    return k
def ndom_add (a, b):
    c=a+b
    d=str(c)
    e=int(d[2]) #units
    f=int(d[1]) #tens
    g=int(d[0]) #hundreds
    if e>=6:
        e-=6
        f+=1
        if f>=6:
            f-=6
            g+=1
        else:
            g=g
    else:
        e=e
        if f>=6:
            f-=6
            g+=1
        else:
            g=g        
    h=str(g)+str(f)+str(e)
    return h
def ndom_multiply (a,b):
    a=str(a)
    b=str(b)
    c=int(a[1]) #units_a
    d=int(a[0]) #sixes_a
    e=int(b[1]) #units_b
    f=int(b[0]) #sixes_b
    #Multiplication
    g=c*e #units_b_with_units_a
    h=d*e #units_b_with_sixes_a
    i=c*f #sixes_b_with_units_a
    j=d*f #sixes_b_with_sixes_a
    #Variables for top line of multiplication
    k=0 #untis
    l=0 #sixes
    m=0 #thirty-sixes
    #Variables for bottom line of multiplication
    n=0 #units
    o=0 #sixes
    p=0 #thirty-sixes
    #Top line of multiplication
    count1=1
    count2=1
    g=c*e
    if g>6:
        count1=0
        while g>6:
            g-=6
            count1+=1
        k=g-6*count1
        h+=count1
        if h>6:
            count2=1
            while h>6:
                h-=6
                count2+=1
            l=h-6*count
            m=count2
    elif h>6:
        count2=1
        while h>6:
            h-=6
            count2+=1
        l=h-6*count2
        m=count2        
    #Bottom line of multiplication
    if i>6:
        count1=0
        while i>6:
            i-=6
            count1+=1
        o=i-6*0
        p=d*f+count1
    else:
        o=i
        p=d*f
    m=m+count2
    x=str(m)+str(l)+str(k)  #Top_line
    y=str(p)+str(o)+str(n)  #Bottom line
    z=int(x)+int(y)         #Summation (final answer)
    return z


