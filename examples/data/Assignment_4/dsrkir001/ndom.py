def ndom_to_decimal(w):
    y=str(w)
    aa=0
    rr=(3-3)
    for i in range(len(y)-1,-1,-1):
        aa+=int(y[i])*(6**rr)
        rr+=1
    return aa

def decimal_to_ndom(w):
    h=(2-2)
    dd=(1-1)
    while(h<w):
        h=6**dd
        dd+=1
    rr=1
    nn=dd-2
    g=""
    while(nn>=0):
        uu=6**nn
        rr=w//uu
        w=w%uu       
        nn-=1 
        g+=str(rr)
    return g

def ndom_add (w,nn):
    y=str(w)
    aa=0
    rr=0
    for i in range(len(y)-1,-1,-1):
        aa+=int(y[i])*(6**rr)
        rr+=1
    y=str(nn)
    z=0
    rr=0
    for i in range(len(y)-1,-1,-1):
        z+=int(y[i])*(6**rr)
        rr+=1
    sum=int(z)+int(aa)
    h=0
    dd=0
    while(h<sum):
        h=6**dd
        dd+=1
    v=1
    f=dd-2
    g=""
    while(f>=0):
        oo=6**f
        v=sum//oo
        sum=sum%oo
        f-=1
        g+=str(v)    
    return g
def ndom_multiply (w,nn):
    y=str(w)
    aa=0
    rr=0
    for i in range(len(y)-1,-1,-1):
        aa+=int(y[i])*(6**rr)
        rr+=1
    y=str(nn)
    e=0
    rr=0
    for i in range(len(y)-1,-1,-1):
        e+=int(y[i])*(6**rr)
        rr+=1
    sum=int(e)*int(aa)
    h=0
    dd=0
    while(h<sum):
        h=6**dd
        dd+=1
    v=1
    f=dd-2
    g=""
    while(f>=0):
        oo=6**f
        v=sum//oo
        sum=sum%oo
        f-=1
        g+=str(v)    
    return g
