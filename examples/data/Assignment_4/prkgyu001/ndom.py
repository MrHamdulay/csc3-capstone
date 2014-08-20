def ndom_to_decimal(a):
    str_version = str(a)
    digit = len(str_version)
    summed = 0
    for i in range(digit):
        if i == 0:
            consecutive = eval(str_version[-(i+1)])
            summed = summed + consecutive
        else:
            consecutive = eval(str_version[-(i+1)])*(6**(i))
            summed = summed + consecutive
    print(summed)
    
        
def decimal_to_ndom(a):
    fourth = int(a/216)
    third = int((a - (fourth*216))/36)
    second = int((a-(216*fourth)-(36*third))/6)
    first = int(a-(216*fourth)-(36*third)-(6*second))
    
    
    final = (str(fourth)+str(third)+str(second)+str(first))
    for digit in final:
        if digit == '0':
            continue
        print(final)


