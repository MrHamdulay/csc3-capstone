def decimal_to_ndom(num):
    ndom = 0
    q = num
    for i in range(0, len(str(num))+1):
        r = q%6
        ndom += r*(10**i)
        q = q//6
    return ndom

def ndom_to_decimal (num):
    startPower = len(str(num))-1
    decimal = 0
    for j in range(startPower,-1,-1):
        #j holds power of 10 in descending order
        digit = num//(10**j)
        num = num%(10**j)
        decimal *= 6
        decimal += digit
    return decimal
    
def ndom_add (num1, num2):
    n1 = ndom_to_decimal(num1)
    n2 = ndom_to_decimal(num2)
    Sum = n1 + n2
    return decimal_to_ndom(Sum)

def ndom_multiply (num1, num2):
    product = 0
    numD1 = ndom_to_decimal(num1)
    numD2 = ndom_to_decimal(num2)
    product = numD1*numD2
    product = decimal_to_ndom(product)
    return product