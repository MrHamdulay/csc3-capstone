# Ndom

def decimal_to_ndom(a):
    l = -1
    u = 5
    i = 0
    if a>35:
        i = 10  
    if a>71:
        i = 20
    if a> 107:
        i = 30
    if a>143:
        i = 40
    if a>179:
        i = 50
    if a>215:
        i = 160
    if a>251:
        i = 170
    if a>287:
        i = 180
    if a>323:
        i = 190
    if a>359:
        i = 200
    if a>395:
        i = 210
    if a>431:
        i = 320
    if a>467:
        i = 330
    if a>503:
        i = 340
    if a>539:
        i = 350
    if a>575:
        i = 360
    if a>611:
        i = 370
    if a>647:
        i = 380
    if a>683:
        i = 490
    while True:
        if a>l and a<=u:
            return (a+(i*4))
            break
        l = l+6
        u = u+6
        i = i+1

def ndom_to_decimal(b):
    for i in range(1000):
        n = decimal_to_ndom(i)
        if b==n:
            return i

def ndom_add(c,d):
    c = decimal_to_ndom(c)
    d = decimal_to_ndom(d)
    return c+d

def ndom_multiply(x,y):
    x = decimal_to_ndom(x)
    y = decimal_to_ndom(y)
    return x*y    