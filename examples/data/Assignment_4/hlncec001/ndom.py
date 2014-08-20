def ndom_to_decimal(a): 
    if len(str(a))==1:
        h= '0'
        t= '0'
        u= str(a)[0]
    if len(str(a))==2:
        h= '0'
        t= str(a)[0]
        u= str(a)[1]
    if len(str(a))==3:
        h= str(a)[0]
        t= str(a)[1]
        u= str(a)[2]
    
    h10= eval(h)*36
    t10= eval(t)*6
    u10= eval(u)*1
    return h10 + t10 + u10
    
def decimal_to_ndom(a): 
    u= a//6
    t= u//6
    h= t//6
    th= h//6
    un= a-(u*6)
    tn= (u-(t*6))*10
    hn= (t-(h*6))*100
    thn= (h-(th*6))*1000
    return thn + hn + tn + un
    
def ndom_add(a, b):
    if len(str(a))==1:
        ha= '0'
        ta= '0'
        ua= str(a)[0]
    if len(str(a))==2:
        ha= '0'
        ta= str(a)[0]
        ua= str(a)[1]
    if len(str(a))==3:
        ha= str(a)[0]
        ta= str(a)[1]
        ua= str(a)[2]
    if len(str(b))==1:
        hb= '0'
        tb= '0'
        ub= str(b)[0]
    if len(str(b))==2:
        hb= '0'
        tb= str(b)[0]
        ub= str(b)[1]
    if len(str(b))==3:
        hb= str(b)[0]
        tb= str(b)[1]
        ub= str(b)[2]
    u= decimal_to_ndom(eval(ua) + eval(ub))
    t= decimal_to_ndom(eval(ta) + eval(tb))*10
    h= decimal_to_ndom(eval(ha) + eval(hb))*100
    return h + t + u

def ndom_multiply(a, b):
    if len(str(a))==1:
        ha= '0'
        ta= '0'
        ua= str(a)[0]
    if len(str(a))==2:
        ha= '0'
        ta= str(a)[0]
        ua= str(a)[1]
    if len(str(a))==3:
        ha= str(a)[0]
        ta= str(a)[1]
        ua= str(a)[2]
    if len(str(b))==1:
        hb= '0'
        tb= '0'
        ub= str(b)[0]
    if len(str(b))==2:
        hb= '0'
        tb= str(b)[0]
        ub= str(b)[1]
    if len(str(b))==3:
        hb= str(b)[0]
        tb= str(b)[1]
        ub= str(b)[2]
    u= str(decimal_to_ndom(eval(ua) * eval(ub)))
    t= str(decimal_to_ndom(eval(ta) * eval(ub)) + eval(u)//10)
    h= decimal_to_ndom(eval(ha) * eval(ub)) + ((eval(t)//10)*(eval(u)//10))
    m= eval(u[-1]) + eval(t[-1])*10 + h*100
    u1= str(decimal_to_ndom(eval(ua) * eval(tb)))
    t1= str(decimal_to_ndom(eval(ta) * eval(tb)) + eval(u1)//10)
    h1= decimal_to_ndom(eval(ha) * eval(tb)) + eval(t1)//10
    m1= eval(u1[-1])*10 + eval(t1[-1])*100 + h1*1000
    u2= str(decimal_to_ndom(eval(ua) * eval(hb)))
    t2= str(decimal_to_ndom(eval(ta) * eval(hb)) + eval(u2)//10)
    h2= decimal_to_ndom(eval(ha) * eval(hb)) + eval(t2)//10
    m2= eval(u2[-1])*100 + eval(t2[-1])*1000 + h2*10000
    return ndom_add(ndom_add(m,m1),m2)