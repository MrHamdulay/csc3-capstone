def decimal_to_ndom(a):
    empty = ""
    while a/6 != 0:
        rem = a%6
        a = a//6
        empty = empty+str(rem)
    empty=(empty[-1::-1])
    return(empty)

def ndom_to_decimal(a):
    m = 1
    n = 1
    string = str(a)
    m = 1-m
    n = 1-n
    for i in (string):
        i=eval(i)
        m = m+i
        n = n+1
        length = len(string)
        if n == length:
            break
        else:
            m = m*6
    return(m)    
            
def ndom_multiply(a,b):
    dec1 = ndom_to_decimal(a)
    dec2 = ndom_to_decimal(b)
    multi = (dec1)*(dec2)
    change = decimal_to_ndom(multi)
    return(change)

def ndom_add(a,b):
    dec1 = ndom_to_decimal(a)
    dec2 = ndom_to_decimal(b)
    add = dec1+dec2
    change = decimal_to_ndom(add)
    return(change)
            