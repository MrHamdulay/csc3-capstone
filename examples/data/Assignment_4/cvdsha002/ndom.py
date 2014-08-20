#Shahrain Coovadia
#CVDSHA002
def ndom_to_decimal(a):
    a=str(a)
    u=0
    p=0
    for x in a[::-1]:
        p+=((eval(x)*(6**u)))
        u=u+1
    return p
def decimal_to_ndom(a):
    q=0
    for i in range(0,len(str(a))+1):
        z=a%6
        q+=z*(10**i)
        a=a//6
    return q
def ndom_add(a,b):
    a,b=ndom_to_decimal(a), ndom_to_decimal(b)
    c=a+b
    return decimal_to_ndom(c)
def ndom_multiply(a,b):
    a,b=ndom_to_decimal(a),ndom_to_decimal(b)
    c=a*b
    return decimal_to_ndom(c)
