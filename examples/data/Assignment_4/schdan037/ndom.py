def decimal_to_ndom(a):
    # base 10 to base 6
    n = -1
    if len(str(a)) == 1:
        if a <= 5:
            return a
        else:
            n = 10
            n += a-6
    elif len(str(a)) == 2:
        hundreds = a//36
        r = a%36
        tens = r//6
        r = r%6
        n = hundreds*100 + tens * 10 + r
        
    elif len(str(a)) == 3:
        thousands = a//216
        r = a%216
        hundreds = r//36
        r = r%36
        tens = r//6
        r = r%6
        n = thousands*1000 + hundreds*100 + tens * 10 + r        
        
    return n

def ndom_to_decimal(a):
    # base 6 to base 10
    n = -1
    if (len(str(a)) == 1):
        n = a
    elif (len(str(a)) == 2):
        n = int(str(a)[0])*6 
        n += int(str(a)[1])
    elif (len(str(a)) == 3):
        n = int(str(a)[0])*36
        n += int(str(a)[1])*6
        n += int(str(a)[2])
    return n

def ndom_add(a, b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    n = x+y
    return decimal_to_ndom(n)

def ndom_multiply(a, b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    n = x*y
    return decimal_to_ndom(n)


