"""Functions for simple Ndom language arithmetic
Nosipho Khumalo
31 March 2014 """

def ndom_to_decimal(a):
    base = str(a)[0]
    if len(str(a)) > 1:
        for i in range(1, len(str(a))):
            decimal = int(base) * 6
            base = decimal + int(str(a)[i])
        return base
    elif len(str(a)) == 1:
        return base
    
def decimal_to_ndom(a):
    div = a//6
    rem = a%6
    ndom = str(rem)
    while div >0:
        rem = div%6        
        div = div//6
        ndom = str(rem) + ndom
    return ndom


def ndom_add(a,b):
    sum = a + b
    sum = str(sum)
    output = ''
    list = [ch for ch in sum]
    for i in range(len(sum)-1,-1,-1):
        list[i] = decimal_to_ndom(int(list[i]))
        if len(list[i]) > 1:
            list[i-1] = str(int(list[i-1]) + int(list[i][0]))
            list[i] = list[i][-1]
        output = list[i] + output
    return output


def ndom_multiply(a,b):
    b = str(b)
    a = str(a)
    sum = 0
    total = 0
    x = len(a) -1
    y = len(b) -1
    for i in range(len(a)):
        sum += int(a[i]) * 6**x
        x -= 1
    for i in range(len(b)):
        total += int(b[i]) * 6**y
        y -= 1    
    product = decimal_to_ndom(sum*total)
    return product
#ndom_multiply(13,14)