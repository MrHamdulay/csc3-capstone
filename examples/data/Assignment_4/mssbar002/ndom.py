def decimal_to_ndom(num):
    quotient = num//6
    remainder = num%6
    remainderStr = ""
    remainderStr += str(remainder)
    while quotient > 0:
        remainder = quotient%6 
        quotient = quotient//6
        remainderStr += str(remainder) 
    number = int(remainderStr[::-1])
    return number

def ndom_to_decimal(num):
    numStrReverse = str(num)[::-1]
    digitSum = 0
    for i in range(len(numStrReverse)):
        digit = int(numStrReverse[i]) * 6**i
        digitSum += digit
    return digitSum

def ndom_add(a, b):
    sumStr = ""
    pow1A = a%10
    pow1B = b%10
    if (pow1A + pow1B) < 6:
        pow1Sum = pow1A + pow1B
        sumStr += str(pow1Sum)
        carry = 0
    else:
        pow1Sum = 0
        sumStr += str(pow1Sum)
        carry = 1
    
    pow2A = (a%100)//10
    pow2B = (b%100)//10
    if (pow2A + pow2B) < 6:
        pow2Sum = pow2A + pow2B
        sumStr += str(pow2Sum + carry)
        carry = 0
    else:
        pow2Sum = 0
        sumStr += str(pow2Sum + carry)
        carry = 1

    pow3A = (a%1000)//100
    pow3B = (b%1000)//100
    if (pow3A + pow3B) < 6:
        pow3Sum = pow3A + pow3B
        sumStr += str(pow3Sum + carry)
        carry = 0
    else:
        pow3Sum = 0
        sumStr += str(pow3Sum + carry)
        carry = 1
        sumStr += '1'

    sum = int(sumStr[::-1])    
    return sum
    
def ndom_multiply(a, b):
    aBase10 = ndom_to_decimal(a)
    bBase10 = ndom_to_decimal(b)
    
    productBase10 = aBase10 * bBase10
    productBase6 = decimal_to_ndom(productBase10)
    
    return productBase6
    
