"""ndom_to_decimal (a), that converts a Ndom number to decimal
decimal_to_ndom (a), that converts a decimal number to Ndom
ndom_add (a, b), that adds 2 Ndom numbers
ndom_multiply (a, b), that multiples 2 Ndom numbers"""
import math
def ndom_to_decimal(number):
    multiple_100 = (number//100)
    times_36 = multiple_100 * 36
    divide_100 = number - (multiple_100 * 100)
    multiple_6 = divide_100// 10
    if( multiple_100 == 0 and multiple_6 == 0):
        returned1 = (number - (4 * (multiple_6 -1)))
        return returned1
    
    if(multiple_100 == 0):
        returned = (number - (4 * (multiple_6)))
        return returned
    
    if(multiple_100 > 0):    
        multiple_4 = (multiple_6 )  * 4
        original = divide_100 - multiple_4
        original_number = times_36 + original
        return original_number

    
def decimal_to_ndom(number):
    senary = 0
    multiple_100 = (number//36)
    lose_difference = multiple_100 * 36
    new_num = number - lose_difference
    multiple_6 = (new_num//6)
    difference_4 = multiple_6 * 4
    Senary_Number = (multiple_100 * 100) + new_num + difference_4
    return Senary_Number

def ndom_add(a,b):
    ConvertA = ndom_to_decimal(a)
    ConvertB = ndom_to_decimal(b)
    NewNum = ConvertA + ConvertB
    FinalNumber = decimal_to_ndom(NewNum)
    return FinalNumber
    
    
def ndom_multiply(a,b):
    ConvertA = ndom_to_decimal(a)
    ConvertB = ndom_to_decimal(b)
    NewNum = ConvertA * ConvertB
    FinalNumber = decimal_to_ndom(NewNum)
    return FinalNumber

