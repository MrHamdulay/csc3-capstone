
def ndom_to_decimal(a):
    if a == 0:
        return 0
    a = str(a)
    ans = int(a[0])
    for i in a[1:]:
        ans *= 6
        ans += int(i)
    return ans
	
def decimal_to_ndom(a):
    n1 = a % 6
    n2 = n1 % 6
    n3 = n2 % 6
    n = str(n1) + str(n2) + str(n3)
    ndom = int(n)
    return ndom

def ndom_add(a, b):
    sum = decimal_to_ndom(a) + decimal_to_ndom(b)
    return sum

def ndom_multiply(a, b):
    product = decimal_to_ndom(a) + decimal_to_ndom(b)
    return product