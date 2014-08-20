def ndom_to_decimal(a):
    x=0
    j=0
    a=str(a)
    for i in (a):
        i=eval(i)
        x=x+i
        j=j+1
        if j==len(a):
            break
        else:
            x=x*6
    return(x)    
            

def decimal_to_ndom(a):
    cheese=""
    while a/6 != 0:
        x=a%6
        a=a//6
        cheese=cheese+str(x)
    return(cheese[-1::-1])
    

def ndom_add(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    total=x+y
    convert=decimal_to_ndom(total)
    return(convert)
            

def ndom_multiply(a,b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    product=x*y
    convert=decimal_to_ndom(product)
    return(convert)


