def ndom_to_decimal(a):
    a=str(a)
    rev_num=a[::-1]
    e=0
    result=0
    for i in rev_num:
        #print(result, i, e)
        result+=(int(i))*(6**e)
        e+=1
    return result
def decimal_to_ndom(a):
    e=0
    result=""
    while a > 0 :
        rem = a%6
        result += str(rem)   #a%6
        a = a//6
    return result[::-1]
def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    z=a+b
    e=0
    result=""
    while z > 0 :
        rem = z%6
        result += str(rem)   #a%6
        z = z//6    
    return result[::-1]
def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    z=a*b
    e=0
    result=""
    while z > 0 :
        rem = z%6
        result += str(rem)   #a%6
        z = z//6    
    return result[::-1]