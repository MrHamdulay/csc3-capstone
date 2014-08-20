#program to convert numbers from base 6 to base 10
def ndom_to_decimal (a):
    if 100<(a)<=1000:
        a=str(a)
        frst=a[0:1]
        scnd=a[1:2]
        thrd=a[2:3]
        ndom=(eval(frst)*36)+(eval(scnd)*6)+(eval(thrd)*1)
        
    elif 10<(a)<100:
        a=str(a)
        frst=a[0:1]
        scnd=a[1:2]
        ndom=(eval(frst)*6)+(eval(scnd)*1)
        
    elif 10<(a)<10:
        a=str(a)
        frst=a[0:1]
        ndom=(eval(frst)*1)
    return ndom

def decimal_to_ndom(x):
    a=x//6
    b=x%6
    c=a//6
    d=a%6
    e=c//6
    f=c%6
    g=e//6
    h=e%6
    j=int(str(h)+str(f)+str(d)+str(b))
    #l=int(j)  
    return j


def ndom_add (a, b):
    #convert number to base 6 first
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a+b
    #d=ndom.ndom_to_decimal(c)
    d=decimal_to_ndom(c)
    return d

def ndom_multiply (a, b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a*b
       #d=ndom.ndom_to_decimal(c)
    d=decimal_to_ndom(c)
    return d    
    