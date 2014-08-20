def decimal_to_ndom(deci):
    q = deci
    r = 1
    x=""
    while q > 0:
        r = q%6
        q = q//6
        x += str(r)
        y= int(x[::-1])
    return y
  
def ndom_to_decimal(ndom):
    ndom = str(ndom)
    suM = 0
    for i in range(len(ndom)):
        lastD = int(ndom[-1])
        ndom = ndom[:-1]
        suM += (lastD)*(6**i)
    return suM

def ndom_add (a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    sum = a + b
    sum = decimal_to_ndom(sum)
    return sum

def ndom_multiply(a, b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    product = x*y
    product=decimal_to_ndom(product)
    return product