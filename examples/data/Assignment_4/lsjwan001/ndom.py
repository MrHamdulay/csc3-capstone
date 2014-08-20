def decimal_to_ndom(a):
    nd=""
    while a!=0:
        nd=str(a%6)+nd
        a=a//6
    
    return nd
 
def ndom_to_decimal(a):
    dec=""
    n=str(a)
    n=n[::-1]
    x=0
    new_num=0
    for i in n:
        nn=int(i)
        dec=nn*6**x
        x+=1
        new_num+=dec
    return new_num

def ndom_add(a,b):
    b=ndom_to_decimal(b)
    a=ndom_to_decimal(a)
    answer=a+b
    answer=decimal_to_ndom(answer)
    return answer

def ndom_multiply(a,b):
    b=ndom_to_decimal(b)
    a=ndom_to_decimal(a)
    answer=a*b
    answer=decimal_to_ndom(answer)
    return answer