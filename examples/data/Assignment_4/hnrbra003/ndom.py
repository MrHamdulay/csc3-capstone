def ndom_add (num1, num2):                                #n = number
    temp1 = ndom_to_decimal(num1)
    temp2 = ndom_to_decimal(num2)
    return decimal_to_ndom(temp1 + temp2)
def decimal_to_ndom(num):
    temp = (num//36 * 100) + ((num%36)//6 * 10) + num%6
    return temp    
def ndom_multiply (num1, num2):
    temp1 = ndom_to_decimal(num1)
    temp2 = ndom_to_decimal(num2)
    return decimal_to_ndom(temp1 * temp2)    
def ndom_to_decimal (num):                           
    temp = (num//100*36) + ((num%100)//10*6) + num%10
    return temp