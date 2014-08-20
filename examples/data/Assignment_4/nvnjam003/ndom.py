def ndom_to_decimal (a):
    stringA = str(a)
    newA = 0
    for x in range (len(stringA)-1, -1, -1):
        newA += int(stringA[x])*(6**(len(stringA)-x-1))
    return newA

def decimal_to_ndom (a):
    decimal = 0
    ndom = 0
    power = 2
    while (decimal < a):
        while (6**power + decimal <= a):
            decimal += 6**power
            ndom += 10**power
        power += -1
    return ndom

def ndom_add(a, b):
    decimalA = ndom_to_decimal(a)
    decimalB = ndom_to_decimal(b)
    return decimal_to_ndom(decimalA + decimalB)

def ndom_multiply(a, b):
    decimalA = ndom_to_decimal(a)
    decimalB = ndom_to_decimal(b)
    return decimal_to_ndom(decimalA*decimalB)
     