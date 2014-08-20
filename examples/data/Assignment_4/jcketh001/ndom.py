def ndom_to_decimal(a):
    output = 0
    iter = str(a)
    for digit in iter:
        output += int(digit) * 6
    return output

def decimal_to_ndom(a):
    output = ''
    while a:
        r, a = a % 6 , a // 6
        output += str(r)
    return int(output[::-1])

def ndom_add(a,b):
    da, db = ndom_to_decimal(a), ndom_to_decimal(b)
    return decimal_to_ndom(da + db)

def ndom_multiply(a,b):
    da, db = ndom_to_decimal(a), ndom_to_decimal(b)
    return decimal_to_ndom(da * db)
