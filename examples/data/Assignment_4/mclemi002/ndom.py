def ndom_to_decimal (a):

    a=str(a)
    if len(a)==3:
        return 36*eval(a[0])+6*eval(a[1])+eval(a[2])
    if len(a)==2:
        return 6*eval(a[0])+eval(a[1])
    else:
        if eval(a)<=5:
            return eval(a)
        else:
            return eval(a)+4
           
def decimal_to_ndom (a):

    a=str(a)
    if int(a)>=36:
        dec=((eval(a)//36)*100)+(eval(a)%36//6*10)+((eval(a)%36)%6)
        return dec
    elif int(a)>5:
        dec=(eval(a)//6)*10+(eval(a)%6)
        return dec
    else:
        return eval(a)
       
    
def ndom_add (a, b):

    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    c=x+y
    c=str(c)
    val=decimal_to_ndom(c)
    return val
 
def ndom_multiply (a, b):

    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    c=(x*y)
    c=str(c)
    val=decimal_to_ndom(c)
    return val