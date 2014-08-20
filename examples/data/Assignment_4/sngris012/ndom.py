def ndom_to_decimal(a):
    j=str(a)
    b=0
    x=0
    for i in range(len(j)-1,-1,-1):
        b+=int(j[i])*(6**x)
        x+=1
    return b

def decimal_to_ndom(a):
    p=0
    q=0
    while(p<a):
        p=6**q
        q+=1
    t=1
    k=q-2
    z=""
    while(k>=0):
        l=6**k
        t=a//l
        a=a%l        
        k-=1 
        z+=str(t)
    return z

def ndom_add (a,c):
    j=str(a)
    b=0
    x=0
    for i in range(len(j)-1,-1,-1):
        b+=int(j[i])*(6**x)
        x+=1
    j=str(c)
    e=0
    t=0
    for i in range(len(j)-1,-1,-1):
        e+=int(j[i])*(6**t)
        t+=1
    sum=int(e)+int(b)
    p=0
    q=0
    while(p<sum):
        p=6**q
        q+=1
    tt=1
    f=q-2
    k=""
    while(f>=0):
        l=6**f
        tt=sum//l
        sum=sum%l
        f-=1
        k+=str(tt)    
    return k
def ndom_multiply (a,c):
    j=str(a)
    b=0
    t=0
    for i in range(len(j)-1,-1,-1):
        b+=int(j[i])*(6**t)
        t+=1
    j=str(c)
    e=0
    t=0
    for i in range(len(j)-1,-1,-1):
        e+=int(j[i])*(6**t)
        t+=1
    sum=int(e)*int(b)
    p=0
    q=0
    while(p<sum):
        p=6**q
        q+=1
    tt=1
    f=q-2
    k=""
    while(f>=0):
        l=6**f
        tt=sum//l
        sum=sum%l
        f-=1
        k+=str(tt)    
    return k
