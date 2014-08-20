def ndom_to_decimal (a):
    ans = 0
    for i in range(0,len(str(a))):
        ans += eval(str(a)[len(str(a))-i-1:len(str(a))-i])*(6**i)
    return ans
def decimal_to_ndom (a):
    ans = 0
    while a >= 36:
        a -= 36
        ans += 100        
    while a >= 6:
        a -= 6
        ans += 10   
    return ans + a
def ndom_add (a, b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
def ndom_multiply (a, b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))