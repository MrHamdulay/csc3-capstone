# This is a module called ndom.py and contains the four functions:
# Ndom is a language where, numbers use only the digits 0-5,
# such that instead of "tens" and "hundreds", 
# the second and third digits represents multiples of 6 and 36 respectively

# ndom_to_decimal (a), that converts a Ndom number to decimal
# decimal_to_ndom (a), that converts a decimal number to Ndom
# ndom_add (a, b), that adds 2 Ndom numbers
# ndom_multiply (a, b), that multiples 2 Ndom numbers

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 28 March 2014

# This function converts a Ndom number to decimal
def ndom_to_decimal(a):
    # Passes parameter to a local variable and converts it to a string
    hand = str(a)
    # switches the base 5 number around
    handler = hand[::-1]
    decimal = 0
    
    # for loop converts base 5 number to decimal
    for i in range(len(handler)):
        decimal = decimal + int(handler[i]) * (6**i)
        
    return decimal


# This function converts a decimal number to Ndom
def decimal_to_ndom(a):
    # Passes parameter to a local variable
    hand = int(a)
    # Passes parameter to variable to be manipulated
    ans = hand
    
    rem = 0
    remstr = ''
    base5 = 0
    
    while ans != 0:
        rem = ans % 6
        # Adds the remainder to a string variable
        remstr = remstr + str(rem)      
        ans = ans // 6
        
    base5 = int(remstr[::-1])
    
    return base5

# This function adds 2 Ndom numbers
def ndom_add(a,b):
    # Passes parameters to local variables
    adda, addb = int(a), int(b)
    
    # does the addition in base 10 after converting from base 5
    add1 = ndom_to_decimal(adda) + ndom_to_decimal(addb)
    add = decimal_to_ndom(add1)
    
    return add

# This function multiples 2 Ndom numbers
def ndom_multiply(a,b):
    # Passes parameters to local variables
    multa, multb = int(a), int(b)
    
    # does the multiplication in base 10 after converting from base 5
    mult1 = ndom_to_decimal(multa) * ndom_to_decimal(multb)
    mult = decimal_to_ndom(mult1)
    
    return mult

# Sample I/O:

# Choose test:
# d 12
# calling function
# called function
# 20
# Sample I/O:

# Choose test:
# n 20
# calling function
# called function
# 12
# Sample I/O:

# Choose test:
# a 123 141
# calling function
# called function
# 304
# Sample I/O:

# Choose test:
# m 13 14
# calling function
# called function
# 230