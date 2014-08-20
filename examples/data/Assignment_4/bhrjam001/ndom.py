def dec2sen(a):
    output = ''
    while a:
        rem, a = a % 6, a // 6
        output += str(rem)
    return int(output[::-1]) if output else 0

def sen2dec(a):
    a, out = str(a), 0
    for i, digit in enumerate(reversed(a)):
        out += int(digit) * (6**i)
    return out

def ndom_to_decimal(a):
    return sen2dec(a)
    
def decimal_to_ndom(a):
    return dec2sen(a)
    
def ndom_add(a, b):
    return dec2sen(sen2dec(a) + sen2dec(b))

def ndom_multiply(a, b):
    return dec2sen(sen2dec(a) * sen2dec(b))
    
    
    