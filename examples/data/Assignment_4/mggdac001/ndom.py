def decimal_to_ndom(a):
    num = a
    x = len(str(num))
    a = 1
    b = 0
    for i in range(x):
        a1 = int(str(num)[i]) * 6**(x-a)
        a = a+1
        b = b+a1
    return b
    
def ndom_to_decimal(a):
    num = a
    
    a = num//6
    b = a//6
    c = b//6
    d = c//6
    
    u = num - a*6
    ut = a - b*6
    uh = b - c*6
    uth = c - d*6
    
    answer = u*1 + ut*10 + uh*100 + uth*1000
    return answer   
    
def ndom_add (a, b):
    x = len(str(a))
    a0 = 1
    b0 = 0
    for i in range(x):
        a1 = int(str(a)[i]) * 6**(x-a0)
        a0 = a0+1
        b0 = b0+a1

    x = len(str(b))
    a00 = 1
    b00 = 0
    for i in range(x):
        a1 = int(str(b)[i]) * 6**(x-a00)
        a00 = a00+1
        b00 = b00+a1
    return b0+b00           

def ndom_multiply (a, b):
    x = len(str(a))
    a0 = 1
    b0 = 0
    for i in range(x):
        a1 = int(str(a)[i]) * 6**(x-a0)
        a0 = a0+1
        b0 = b0+a1
    
    x = len(str(b))
    a00 = 1
    b00 = 0
    for i in range(x):
        a1 = int(str(b)[i]) * 6**(x-a00)
        a00 = a00+1
        b00 = b00+a1
    return b0*b00  