#NGMTAS001
#Tase Ngambi

def ndom_to_decimal (number):
    
    answer = ((number%100)//10*6) + (number//100*36)+ number%10
    return answer

def decimal_to_ndom(number):
    
    answer = ((number%36)//6 * 10) +(number//36*100)+ number%6
    return answer   

def ndom_add (value1, value2):
    
    decimal1 = ndom_to_decimal(value1)
    decimal2 = ndom_to_decimal(value2)
    
    answer = decimal_to_ndom(decimal1+decimal2)
    return answer

def ndom_multiply (value1, value2):
    
    decimal1 = ndom_to_decimal(value1)
    decimal2 = ndom_to_decimal(value2)
    
    answer = decimal_to_ndom(decimal1*decimal2)
    return answer
