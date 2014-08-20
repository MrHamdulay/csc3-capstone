def decimal_to_ndom(a):
    b = [0,0,0]
    while a != 0:
        b[0] += 1
        if b[0]//6 != 0:
            b[1] += 1
            b[0] = 0
        if b[1]//6 != 0:
            b[2] += 1
            b[1] = 0
        a += -1
    newnum = str(b[2])+str(b[1])+str(b[0])
    return int(newnum)
    
def ndom_to_decimal(a):
    a = str(a)
    decimalnum = 0
    for i in range(len(a),0,-1):
        decimalnum += eval(a[i-1])*(6**(len(a)-i))
    return decimalnum        

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    result = a+b
    return decimal_to_ndom(result)

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    result = a*b
    return decimal_to_ndom(result)