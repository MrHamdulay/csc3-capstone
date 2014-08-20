def ndom_to_decimal(a):
    x=str(a)
    b=0
    t=0
    for i in range(len(x)-1,-1,-1):
        b+=int(x[i])*(6**t)
        t+=1
    return b

def decimal_to_ndom(a):
    p=0
    q=0
    while(p<a):
        p=6**q
        q+=1
    t=1
    c=q-2
    k=""
    while(c>=0):
        l=6**c
        t=a//l
        a=a%l        
        c-=1 
        k+=str(t)
    return k

def ndom_add (a,c):
    x=str(a)
    b=0
    t=0
    for i in range(len(x)-1,-1,-1):
        b+=int(x[i])*(6**t)
        t+=1
    x=str(c)
    e=0
    t=0
    for i in range(len(x)-1,-1,-1):
        e+=int(x[i])*(6**t)
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
    x=str(a)
    b=0
    t=0
    for i in range(len(x)-1,-1,-1):
        b+=int(x[i])*(6**t)
        t+=1
    x=str(c)
    e=0
    t=0
    for i in range(len(x)-1,-1,-1):
        e+=int(x[i])*(6**t)
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
