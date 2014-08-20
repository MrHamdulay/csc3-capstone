#program to convert decimal number to ndom arithmatic and back
#kennedy muranda
#01-04-2014

def ndom_to_decimal(k):
    if k >= 100:
        Hundereds = k//100
        Leftover = k%100
        Tens = Leftover//10
        Units = Leftover%10
        Decimal_Number = (Hundereds*36) + (Tens*6) + Units
    
    elif (10 <= k < 100):
        Tens = k//10
        Units = k%10
        Decimal_Number = (Tens*6) + Units
        
    else:
        Units = k%10
        Decimal_Number = Units
        
    return Decimal_Number
        


def decimal_to_ndom(k):
    if k >= 36:
        Hundereds = k//36
        Leftover = k%36
        Tens = Leftover//6
        Units = Leftover%6
        Ndom_Number = (Hundereds*100) + (Tens*10) + Units
              
    elif (6 <= k < 36):
        Tens = k//6
        Units = k%6
        Ndom_Number = (Tens*10) + Units
            
    else:
        Units = k%6
        Ndom_Number = Units
            
    return Ndom_Number    
    


def ndom_add(k,b):
    k = ndom_to_decimal(k)
    b = ndom_to_decimal(b)
    
    Decimal_Addition = k + b
    
    Final = decimal_to_ndom(Decimal_Addition)
    
    return Final 
    

def ndom_multiply(k,b):
    k = ndom_to_decimal(k)
    b = ndom_to_decimal(b)  
    
    Decimal_Multiplication = k*b
    
    Final = decimal_to_ndom(Decimal_Multiplication)
    
    return Final






