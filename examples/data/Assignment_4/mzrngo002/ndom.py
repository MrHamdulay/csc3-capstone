def ndom_to_decimal (a):
    x=len(str(a))-1
    y=0
    for i in str(a):
        y=6**x*int(i)+y
        x-=1
    return y

        
def decimal_to_ndom (a):
    x=""
    while a!=0:
        x=x+str(a%6)
        a//=6
    z=int(x[::-1])
    return z
    

def ndom_add (a, b):
    a=ndom_to_decimal (a)
    b=ndom_to_decimal (b)
    c=a+b
    return decimal_to_ndom (c)

def ndom_multiply (a, b):
    a=ndom_to_decimal (a)
    b=ndom_to_decimal (b)
    d=a*b
    return decimal_to_ndom (d)