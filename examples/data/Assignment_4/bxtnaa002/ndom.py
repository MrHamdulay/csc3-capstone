# ndom.py
# author: bxtnaa002

def ndom_to_decimal(a):
    a = str(a)
    if len(a)==1:
        a = int(a)
        return a
    elif len(a)==2:
        o = a[1]
        o = int(o)
        t = a[0]
        t = int(t)
        b = o*1 + t*6
        return b
    elif len(a)==3:
        o = a[2]
        o = int(o)
        t = a[1]
        t = int(t)
        h = a[0]
        h = int(h)
        b = o*1 + t*6 + h*36
        return b
    
    elif len(a)==4:
        o = a[3]
        o = int(o)
        t = a[2] 
        t = int(t)
        h = a[1]
        h= int(h)
        th = a[0]
        th = int(th)
        b = o*1 + t*6 + h*36 + th*216
        return b 
           
def decimal_to_ndom(a):
    th = a//216
    h = (a - th*216)//36
    t = (a - th*216 - h*36)//6
    o = (a - th*216 - h*36 - t*6)//1
    b = th*1000 + h*100 +t*10 + o
    return b
    
import ndom
           
def ndom_add(a,b):
    aNum = ndom.ndom_to_decimal(a)
    bNum = ndom.ndom_to_decimal(b)
        
    c = aNum + bNum      
    cSum = ndom.decimal_to_ndom(c)
    return cSum
     
def ndom_multiply(a,b):
    Anum = ndom.ndom_to_decimal(a)
    Bnum = ndom.ndom_to_decimal(b)
    
    d = Anum*Bnum
    dMult = ndom.decimal_to_ndom(d)
    return dMult
    