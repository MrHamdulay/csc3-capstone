#ndom.py
#vuyolwethu nkosi
#29 march 2014


def ndom_to_decimal(a):
    d_num=(a//100)*36+(a%100//10)*6+a%10
    return d_num


def decimal_to_ndom(a):
    v=a//36
    u=((a%36)//6)
    y=a%6
    
    if v==0:
        v=""
    if u==0 and u==0:
        u=""
    spill=str(v)+str(u)+str(y)
    eval(spill)
    return spill


def ndom_add(a,b):
    d_a=ndom_to_decimal(a)
    d_b=ndom_to_decimal(b)
    w=d_a+d_b
    return decimal_to_ndom(w)


def ndom_multiply(a,b):
    d_a=ndom_to_decimal(a)
    d_b=ndom_to_decimal(b)
    w=d_a*d_b
    return decimal_to_ndom(w)

    
    
    
    
        

        