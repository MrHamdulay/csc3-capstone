# ndom.py
# module with the following functions for simple Ndom arithmetic, 
#   assuming that all values have at most 3 digits
#   def ndom_to_decimal(a)
#     converts a Ndom number to a decimal
#   def decimal_to_ndom(a)
#     converts a decimal number to a Ndom
#   def ndom_add(a, b)
#     adds 2 Ndom numbers    
#   def ndom_multiply(a, b)
#     multiplies 2 Ndom numbers
# Thomas Konigkramer
# 29 March 2014


def ndom_to_decimal(a):
    
    if len(str(a)) == 1:
        ndom = a
        return ndom
    
    if len(str(a)) == 2:
        mult6 = a // 10 * 6
        digit = a % 10
        decimal = mult6 + digit
        return decimal
    
    if len(str(a)) == 3:
        mult36 = a // 100 * 36
        mult6 = (a - a // 100 * 100) // 10 * 6
        digit = (a - a // 100 * 100) % 10
        decimal = mult36 + mult6 + digit
        return decimal

def decimal_to_ndom(a):
    
    if a <= 5:
        ndom = a
        return ndom
    
    if 5 < a < 36:
        undo6 = a // 6 * 10
        digit = a % 6
        ndom = undo6 + digit
        return ndom
    
    if a >= 36:
        undo36 = (a // 36) * 100
        undo6 = ((a - a // 36 * 36) // 6) * 10
        digit = (a - a // 36 * 36) % 6
        ndom = undo36 + undo6 + digit
        return ndom

def ndom_add(a, b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    ans = x + y
    return decimal_to_ndom(ans)

def ndom_multiply(a, b):
    x = ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    product = x * y
    return decimal_to_ndom(product)