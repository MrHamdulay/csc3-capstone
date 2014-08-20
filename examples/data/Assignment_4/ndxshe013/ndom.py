
def ndom_to_decimal(a):
    s = 0
    t = 0
    while True:
        s = ((a%10) * (6**t)) +s
        if a//10 == 0:
            break
        else:
            a = a//10
        t = t +1
    return s

def decimal_to_ndom (a):
    s = ""
    while True:
        s = str(a%6)+s
        if(a//6 == 0):
            break
        else:
            a = a//6
    return s
def ndom_add (a, b):
    a2 = ndom_to_decimal(a)
    b2 = ndom_to_decimal(b)
    return decimal_to_ndom(a2+b2)
def ndom_multiply (a, b):
    a2 = ndom_to_decimal(a)
    b2 = ndom_to_decimal(b)
    return decimal_to_ndom(a2*b2)
