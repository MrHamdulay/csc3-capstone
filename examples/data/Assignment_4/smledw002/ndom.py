def decimal_to_ndom(x):

    tens = x//6
    hundreds = 0
    if tens >5:
        hundreds = x//36
        tens -= 6*hundreds

    deci = x % 6


    return tens*10 + deci + hundreds*100

def ndom_to_decimal(x):

    tens = x//10
    decimals = x%10
    hundreds = 0
    if tens > 10:
        hundreds = x//100
        tens -= hundreds*10

    return tens*6 + decimals +hundreds*36

def ndom_add(a,b):

    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)

    add = a+b

    return decimal_to_ndom(add)

def  ndom_multiply(a, b):

    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)

    multiply = a*b

    return decimal_to_ndom(multiply)







