#Tevin Chetty
#CHTTEV001
#Assignment 4
#ndom

def ndom_to_decimal(a):
    ans = 0
    for i in range(len(str(a))):
        ans += int(str(a)[len(str(a)) - 1 - i]) * 6**i
    return ans

def decimal_to_ndom(a):
    x = ''
    while a != 0:
        x = str(a % 6) + x
        a //= 6
    return x

def ndom_add(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) + ndom_to_decimal(b))

def ndom_multiply(a, b):
    return decimal_to_ndom(ndom_to_decimal(a) * ndom_to_decimal(b))
