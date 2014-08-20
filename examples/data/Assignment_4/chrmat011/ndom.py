def ndom_to_decimal(a):
    s=str(a)
    total=0
    for i in range(len(s)):
        total += (6**i)*(int(s[-1*(i+1)]))
    return(total)

def decimal_to_ndom(a):
    digits=[0]*10
    for i in range(9,-1,-1):
        while 6**i <= a:
            digits[i]+=1
            a-=6**i

    total = ''
    for i in range(9,-1,-1):
        total += str(digits[i])
    return(int(total))

def ndom_add(a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a+b)

def ndom_multiply(a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a*b)
