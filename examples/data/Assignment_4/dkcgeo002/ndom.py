__author__ = 'George'
def ndom_to_decimal (a):
    a = str(a)
    if len(a) == 1:
        return eval(a)
    elif len(a) == 2:
        return int(a[0])*6+int(a[1])
    else:
        return int(a[0])*36+int(a[1])*6+int(a[2])
def decimal_to_ndom (a):
    a = str(a)
    next = int(a)
    result = ""
    while next != 0:
        result = str(next%6)+result
        next = next//6
    return int(result)
def ndom_add (a, b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
def ndom_multiply (a, b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))