def change_base(n, a, b):
    ret = 0
    ind = 1
    while(n > 0):
        ret += (n%b)*ind
        n //= b
        ind *= a
    return ret

def ndom_to_decimal(ndom):
    return change_base(ndom, 6, 10)

def decimal_to_ndom(num):
    return change_base(num, 10, 6)
    
def ndom_add(a, b):
    dec_sum = ndom_to_decimal(a) + ndom_to_decimal(b)
    return decimal_to_ndom(dec_sum)

def ndom_multiply(a, b):
    dec_pro = ndom_to_decimal(a) * ndom_to_decimal(b)
    return decimal_to_ndom(dec_pro)
