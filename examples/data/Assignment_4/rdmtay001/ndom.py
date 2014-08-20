def ndom_to_decimal(a):
    answer=0
    stringOfNumber=str(a)
    length_of_string=len(stringOfNumber)
    variable_for_for_loop=stringOfNumber[:length_of_string-1]
    
    for x in variable_for_for_loop:
        digit=eval(x)
        answer+=digit
        answer=answer*6
        
        
        #answer+=digit
    lastnumber=len(stringOfNumber)
    valuelastnumber=eval(stringOfNumber[lastnumber-1:lastnumber])
    answer=answer+valuelastnumber
    
    return answer
if __name__=="__ndom_to_decimal__":
    ndom_to_decimal(a)
    
    
def decimal_to_ndom(a):
    ndom=""
    wholeNumber=a
    
   
    while wholeNumber>0:
        remainder=wholeNumber%6
        wholeNumber=wholeNumber//6
        stringDigits=str(remainder)
        ndom=ndom+stringDigits
        
        
    
    final_ndom=ndom[::-1]
    return final_ndom
    
if __name__=="__decimal_to_ndom__":
    decimal_to_ndom(a)
    
def ndom_add(a, b):
    number1= ndom_to_decimal(a)
    number2= ndom_to_decimal(b)
    sum_decimals= number1+number2
    sum_ndom=decimal_to_ndom(sum_decimals)
    return sum_ndom
if __name__=="__ndom_add__":
    ndom_add(a,b)
    
def ndom_multiply(a, b):
    decimal1= ndom_to_decimal(a)
    decimal2= ndom_to_decimal(b)
    product_decimal= decimal1*decimal2
    product_ndom=decimal_to_ndom(product_decimal)
    return product_ndom
if __name__=="__ndom_multiply__":
    ndom_multiply(a,b)
    

        
    
        