# Module that contains functions that convert a number to a ndom vise versa and that give the sum and the product of two ndoms
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 2014/03/29

def decimal_to_ndom(num):
    ndom=''
    while num>5:
        remainder,num  = num%6, num//6,
        remainder = str(remainder)
        ndom += remainder
    ndom+=str(num)
    ndom=ndom[::-1]
    return ndom
    
def ndom_to_decimal (num):
    from math import floor
    num = str(num)
    j = 1
    nber = 0
    for i in num:
        i = int(i)
        nber += floor(i*6**(len(num)-j))
        j+=1
    return nber

def ndom_add (num1, num2):
    n1 = ndom_to_decimal (num1)
    n2 = ndom_to_decimal (num2)
    num = n1 + n2
    num = decimal_to_ndom(num)
    return num

def ndom_multiply (num1, num2):
    n1 = ndom_to_decimal (num1)
    n2 = ndom_to_decimal (num2)
    num = n1 * n2
    num = decimal_to_ndom(num)  
    return num