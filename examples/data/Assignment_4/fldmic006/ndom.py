"""Michael Field
covert 10 decimal number system to 6 digit number system
1 April 2014"""
def ndom_to_decimal(Nnum):
    #convert Nnum to a string
    ndom = str(Nnum)
    
    hundreds = ""
    tens = ""
    units = ""
    
    acNum = 0
    
    #if value > 100
    if(len(ndom) == 3):
        hundreds = ndom[0:1]
        tens = ndom[1:2]
        units = ndom[2:3]
        
        #output actual number
        acNum = int(hundreds)*36 + int(tens)*6 + int(units)
        
    #if 10 < value < 100
    if(len(ndom) == 2):
        tens = ndom[0:1]
        units = ndom[1:2]
                
        #output actual number
        acNum = int(tens)*6 + int(units)    
        
    #if 10
    if(len(ndom) == 1):
        units = ndom[0:1]
                        
        #output actual number
        acNum =int(units)
    
    #return actual number
    return acNum
        
def decimal_to_ndom(Dnum):
    
    rem = 0
    hundreds = 0
    tens = 0
    units = 0
    
    #actual conversions
    hundreds = Dnum//36   
    rem = Dnum%36
    tens = rem//6
    units = rem%6
    
    if(hundreds != 0):
        ndomNo = str(hundreds) + str(tens) + str(units)
    
    elif(tens !=0):
        ndomNo = str(tens) + str(units)
    
    else:
        ndomNo = str(units)
        
    return ndomNo

def ndom_add(num1, num2):
    
    #convert ndom numbers to normal number
    norm1 = ndom_to_decimal(num1)
    norm2 = ndom_to_decimal(num2)
    
    #add normal numbers
    sum1 = norm1 + norm2
    
    #convert sum to ndom
    Nsum = decimal_to_ndom(sum1)
    
    #return the ndom-sum
    return(Nsum)

def ndom_multiply(num1, num2):
    
    #convert ndom numbers to normal number
    norm1 = ndom_to_decimal(num1)
    norm2 = ndom_to_decimal(num2)
    
    #multiply normal numbers
    product = norm1 * norm2
    
    #convert product to ndom
    Nproduct = decimal_to_ndom(product)
    
    #return ndom product
    return Nproduct