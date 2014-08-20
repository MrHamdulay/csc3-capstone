def ndom_to_decimal(f):
    q=str(f)
    w=0
    for i in q[:len(q)-1]:
        w+=int(i)
        w*=6
    y= w +int(q[len(q)-1])
    return y
def decimal_to_ndom(f):
    q=''
    i=f
    while i!=0:
        i=f//6
        q+=str(f%6)
        f=i
    return str(q)[::-1] 
def ndom_add(f,g):
    return decimal_to_ndom(ndom_to_decimal(f)+ndom_to_decimal(g))
def ndom_multiply(f,g):
    return decimal_to_ndom(ndom_to_decimal(f)*ndom_to_decimal(g))