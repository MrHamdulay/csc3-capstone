import math
def decimal_to_ndom(a):
    list_1 = []
    for i in range(0, 3):
        q=a//6
        z=a%6
        a=q
        list_1.append(z)
        list_2=reversed(list_1)
    answer=''.join(str(i) for i in list_2)
    return int(answer)

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
        
        
        
    
        

    