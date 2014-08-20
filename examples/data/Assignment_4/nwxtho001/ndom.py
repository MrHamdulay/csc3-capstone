'''A module to manipulate base-6 numbers.
Written by Tom New on 01/04/14'''

def ndom_to_decimal (x):
    '''Converts a base-6 number to base-10'''
    x = str (x)
    length = len (x)
    y = 0
    for i in range (length):
        y += int (x[i:i+1]) * 6 ** (length - (i+1))
    return y

def decimal_to_ndom (x):
    '''Converts a base-10 number to base-6'''
    remainder = x%6
    quotient = (x-remainder)//6
    y = str (remainder)
    while quotient > 0:
        remainder = quotient%6
        quotient = (quotient-remainder)//6
        y += str (remainder)
    y = int (y[::-1])
    return y

def ndom_add (a, b):
    '''Adds two base-6 numbers'''
    a = ndom_to_decimal (a)
    b = ndom_to_decimal (b)
    total = a + b
    total = decimal_to_ndom (total)
    return total

def ndom_multiply (a, b):
    '''Finds the product of two base-6 numbers'''
    a = ndom_to_decimal (a)
    b = ndom_to_decimal (b)
    prod = a * b
    prod = decimal_to_ndom (prod)
    return prod    

if __name__ == '__main__':
    print (ndom_to_decimal (432))
    print (decimal_to_ndom (164))
    print (ndom_add (14, 24))
    print (ndom_multiply (14, 24))