#program to change ndom number to normal numbers, visa versa, and do addition and multiplication of ndom numbers

def ndom_to_decimal (a):
    
    if a<6:
        a=answer
        return answer
        
    elif a<1000:
        
        hundreds = a//100
        tens = (a%100)//10
        units = a%10
        answer = hundreds*36 + tens*6 +units
        return answer


def decimal_to_ndom (a):
    
    if a<6:
        a=answer
        return answer
        
#337 is decimal value of ndom number 999    
    elif a<=387:
        hundreds = a//36
        tens = (a%36)//6
        units = (a%36)%6
        answer = hundreds*100+tens*10+units
        return answer
        
def ndom_add (a,b):
    
    sum = a+b
    
    hundreds = (sum//100)*100 + ((sum%100)//60)*100
    
    
    #Get tens unit, then minus the tens units that have contributed to an extra hundred and then add the number of times the units divide into 6
    tens = (sum%100)//10*10 - ((sum%100)//60)*6*10 + (sum%10)//6*10
    
    units = (sum%10) - ((sum%10)//6)*6
    
    answer = hundreds + tens + units
    return answer
    
def ndom_multiply (a,b):
    
    #convert ndoms to decimals
        
    if a<6:
        a=a
            
    elif a<1000:
            
        hundreds = a//100
        tens = (a%100)//10
        units = a%10
        a_dec = hundreds*36 + tens*6 +units
        
    if b<6:
        b=b
                    
    elif b<1000:
                    
        hundreds = b//100
        tens = (b%100)//10
        units = b%10
        b_dec = hundreds*36 + tens*6 +units
        
    prod = a_dec*b_dec
    
    #convert prod (decimals) to ndom
    if prod<6:
            print (prod)
            
    #337 is decimal value of ndom number 999    
    elif prod<=387:
        hundreds = prod//36
        tens = (prod%36)//6
        units = (prod%36)%6
        answer = hundreds*100+tens*10+units
        return answer