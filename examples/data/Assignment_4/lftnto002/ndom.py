def decimal_to_ndom(a):
    converted_string, modstring="", ""
    current_num= a
    if not a:
        return "0"
    while current_num:
        mod= current_num % 6
        current_num= current_num // 6
        converted_string = chr(48 + mod + 7 *(mod > 10)) + converted_string
    return converted_string
        
def ndom_to_decimal(a):
    sum=0
    parseNum=str(a)
    indices= range(len(parseNum))
    for i in indices:
        sum+= int(parseNum[i])*6**int(indices[::-1][i])
    return sum
    
def ndom_add(a,b):
    x= ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    answer= x+y
    results= decimal_to_ndom(answer)
    return results

def ndom_multiply(a,b):
    x= ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    answer= x*y
    results= decimal_to_ndom(answer)
    return results

