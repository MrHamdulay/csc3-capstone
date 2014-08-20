#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     28-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def ndom_to_decimal(a):
    decimal = 0
    heximal = 6 ** (len(str(a))-1)
    for i in str(a):
        decimal += eval(i) * heximal
        heximal /= 6
    return int(decimal)

def decimal_to_ndom(a):
    ndom = ""
    remainder = a
    heximal = 36
    for i in range(3):
        ndom += str(remainder//int(heximal))
        remainder = remainder % heximal
        heximal /= 6
    return int(eval(ndom))

def ndom_add(a,b):
    a,b = ndom_to_decimal(a), ndom_to_decimal(b)
    return(int(decimal_to_ndom(a+b)))

def ndom_multiply(a,b):
    a,b = ndom_to_decimal(a), ndom_to_decimal(b)
    return(int(decimal_to_ndom(a*b)))
