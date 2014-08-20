def ndom_to_decimal(a):
    temp=str(a)
    q=0
    for i in temp[:len(temp)-1]:
        q+=int(i)
        q*=6
    y= q +int(temp[len(temp)-1])
    return y
def decimal_to_ndom(a):
    temp=''
    i=a
    while i!=0:
        i=a//6
        temp+=str(a%6)
        a=i
    return str(temp)[::-1] 
def ndom_add(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
def ndom_multiply(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))