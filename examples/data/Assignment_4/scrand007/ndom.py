def ndom_to_decimal (a):
    b = str(a)
    c = len(b)

    if c == 1:
        d = int(a)
    if c == 2:
        d = int(b[0])*6 + int(b[1])
    if c == 3:
        d = int(b[0])*36 +int(b[1])*6 + int(b[2])
    return(d)

def decimal_to_ndom (a):
    b = str(a)
    c = len(b)
    
    if c == 1:
        d = int(a)
    if c == 2:
        e = a//6
        f = a % 6
        g = e//6
        h = e % 6
        i = g//6
        j = g % 6
        d = int(str(j)+str(h)+str(f))
    if c == 3:
        if c == 3:
            if a >= 216:
                e = a//6
                f = a % 6
                g = e//6
                h = e % 6
                i = g//6
                j = g % 6
                k = i//6
                l = i % 6
                d = int(str(l)+str(j)+str(h)+str(f))    
            else:
                e = a//6
                f = a % 6
                g = e//6
                h = e % 6
                i = g//6
                j = g % 6
                d = int(str(j)+str(h)+str(f))    
    return(d)

def ndom_add (num1, num2):
    a = ndom_to_decimal(num1)
    c = ndom_to_decimal(num2)
    d = a + c
    e = decimal_to_ndom(d)
    return(e)

def ndom_multiply (num1,num2):
    a = ndom_to_decimal(num1)
    c = ndom_to_decimal(num2)
    d = a * c
    e = decimal_to_ndom(d)
    return(e)    