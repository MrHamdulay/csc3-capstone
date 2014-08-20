import math
#ndom.py

def ndom_to_decimal(a):
    k = str(a)
    l =[]
    for x in k:
        l.append(x)
    p = 0
    t = 0

    for x in range(len(l)):
        t =t+ int(l.pop())*(6**p)
        p = p+1
    
    return (t)
    
def decimal_to_ndom(a):
    l =[]
    s= ""
    while a > 0:
        l.append(a % 6)
        a = math.floor(a/6)
    for x in range(len(l)):
        s = str(l.pop(0))+s
    return (eval(s))

def ndom_add (a, b):
    return decimal_to_ndom((ndom_to_decimal(a)+ndom_to_decimal(b)))

def ndom_multiply (a, b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))

        
