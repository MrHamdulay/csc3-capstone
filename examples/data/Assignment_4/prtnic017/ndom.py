# Student Number: PRTNIC017
# 28/03/2014


def ndom_to_decimal(a):  # n
    strval = str(a)
    if len(strval) == 4:
        return (int(strval[0]) * 216) + (int(strval[1]) * 36) + (int(strval[2]) * 6) + int(strval[3])
    elif len(strval) == 3:
        return (int(strval[0]) * 36) + (int(strval[1]) * 6) + int(strval[2])
    elif len(strval) == 2:
        return (int(strval[0]) * 6) + int(strval[1])
    else:
        return strval


def decimal_to_ndom(a):  # d
    ndom = ''
    x = 216
    while x >= 6:
        ndom += str(a // x)
        a -= (a // x) * x
        x //= 6
    while ndom.startswith('0'):
        ndom = ndom[1:]
    return ndom + str(a)


def ndom_add(a, b):  # a
    return decimal_to_ndom(ndom_to_decimal(a) + ndom_to_decimal(b))


def ndom_multiply(a, b):  # m
    return decimal_to_ndom(ndom_to_decimal(a) * ndom_to_decimal(b))