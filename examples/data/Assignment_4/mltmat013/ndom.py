def decimal_to_ndom(a):
    ndom = ''
    if a < 36:
        sixes = a//6
        ones = a % 6
        ndom = int(str(sixes) + str(ones))
        #print(ndom)
        return int(ndom)
    if a >= 36:
        thirty_sixes = a//36
        d = a - (thirty_sixes * 36)
        sixes = d//6
        ones = d % 6
        ndom = int(str(thirty_sixes) + str(sixes) + str(ones))
       # print(ndom)
    return int(ndom)

def ndom_to_decimal(a):
    a = str(a)
    decimal = 0
    if len(a) == 3:
        decimal += int(a[0]) * 36
        decimal += int(a[1]) * 6
        decimal += int(a[2])
    if len(a) == 2:
        decimal += int(a[0]) *6
        decimal += int(a[1])
    if len(a) == 1:
        decimal += int(a)
    #print(decimal)
    return decimal

def ndom_add(a,b):
    total = ndom_to_decimal(a) + ndom_to_decimal(b)
    #print(decimal_to_ndom(total))
    return decimal_to_ndom(total)

def ndom_multiply(a,b):
    product = ndom_to_decimal(a) * ndom_to_decimal(b)
    #print(decimal_to_ndom(product))
    return decimal_to_ndom(product)