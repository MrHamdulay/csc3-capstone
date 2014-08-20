def ndom_to_decimal(a):
    sa=str(a)
    if len(sa)==3:
        num = eval(sa[0:1])*36+eval(sa[1:2])*6+eval(sa[2:3])
    elif len(sa)==2:
        num = eval(sa[0:1])*6+eval(sa[1:2])
    else:
        num = eval(sa[0:1])
    return(num)

def decimal_to_ndom(a):
    fir = a//36
    second = (a%36)//6
    third = a-(fir*36+second*6)
    fir,second,third=str(fir),str(second),str(third)
    if(fir)=="0":
        fir=""
    num = eval(fir+second+third)
    return(num)  

def ndom_add(a,b):
    result=decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
    return(result)
    
    
def ndom_multiply(a,b):
    result=decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
    return(result)    
