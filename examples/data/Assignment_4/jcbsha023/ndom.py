#program to convert decimal number to ndom arithmatic and back
#Anthony Jacob
#03-04-2014

def ndom_to_decimal(a):
    if a >= 100:
        Hundereds = a//100
        Leftover = a%100
        Tens = Leftover//10
        Units = Leftover%10
        Decimal_Number = (Hundereds*36) + (Tens*6) + Units
    
    elif (10 <= a < 100):
        Tens = a//10
        Units = a%10
        Decimal_Number = (Tens*6) + Units
        
    else:
        Units = a%10
        Decimal_Number = Units
        
    return Decimal_Number
        


def decimal_to_ndom(a):
    if a >= 36:
        Hundereds = a//36
        Leftover = a%36
        Tens = Leftover//6
        Units = Leftover%6
        Ndom_Number = (Hundereds*100) + (Tens*10) + Units
              
    elif (6 <= a < 36):
        Tens = a//6
        Units = a%6
        Ndom_Number = (Tens*10) + Units
            
    else:
        Units = a%6
        Ndom_Number = Units
            
    return Ndom_Number    
    


def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    
    Decimal_Addition = a + b
    
    Final = decimal_to_ndom(Decimal_Addition)
    
    return Final 
    

def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)  
    
    Decimal_Multiplication = a*b
    
    Final = decimal_to_ndom(Decimal_Multiplication)
    
    return Final






