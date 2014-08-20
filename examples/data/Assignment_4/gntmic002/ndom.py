#assignment 4.2


def ndom_to_decimal(a):
    ans = 0
    l = len(str(a))-1
    for i in str(a):
        ans = ans + int(i)*6**l
        l -= 1
    return ans

def decimal_to_ndom(a):
    s = ""
    while a > 0:
        s = s + str(a%6)
        a=a//6
    return int(s[::-1])

def ndom_add(a, b):
    ans = ndom_to_decimal(a) + ndom_to_decimal(b)
    ans = decimal_to_ndom(ans)
    return ans

def ndom_multiply(a,b):
    ans = ndom_to_decimal(a) * ndom_to_decimal(b)
    ans = decimal_to_ndom(ans) 
    return ans
