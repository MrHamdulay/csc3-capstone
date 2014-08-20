def ndom_to_decimal(d):
    x=str(d)
    y=0
    for i in x[:len(x)-1]:
        y+=int(i)
        y*=6
    z= y+int(x[len(x)-1])
    return z
def decimal_to_ndom(d):
    x=''
    i=d
    while i!=0:
        i=d//6
        x+=str(d%6)
        d=i
    return str(x)[::-1] 
def ndom_add(d,b):
    return decimal_to_ndom(ndom_to_decimal(d)+ndom_to_decimal(b))
def ndom_multiply(d,b):
    return decimal_to_ndom(ndom_to_decimal(d)*ndom_to_decimal(b))

