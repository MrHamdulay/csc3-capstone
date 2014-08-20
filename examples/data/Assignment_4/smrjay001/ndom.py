"""
Assignment 4 - Queestion 2
Jayan Smart
April 2014
"""

def decimal_to_ndom (a):
    x = a%36
    num1 = (a-x)//36
    num1 = str(num1)
    y = x%6
    num2 = (x-y)//6
    num2 = str(num2)
    num3 = str(y)
    
    if eval(num1) == 0:
        if eval(num2) == 0:
            num = (num3)
        else:
            num = (num2+num3)
    else:
        num = (num1+num2+num3)
    num = eval(num)
    return (num)
    
def ndom_to_decimal (a):
    x = (a-(a%100))
    y = ((a-x)-(a%10))
    z = (a-(x+y))
    x = x//100 * 36
    y = y//10 * 6
    
    if x == 0:
        if y == 0:
            num = (z)
        else:
            num = (y+z)
    else:
        num = (x+y+z)
    
    return (num)

def ndom_add (a, b):
    a = ndom_to_decimal (a)
    b = ndom_to_decimal (b)
    num = a+b
    num = decimal_to_ndom (num)
    return (num)
    
def ndom_multiply (a, b):
    a = ndom_to_decimal (a)
    b = ndom_to_decimal (b)
    num = a*b
    num = decimal_to_ndom (num)
    return (num)    