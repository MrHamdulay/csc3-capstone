# Functions for ndom calculations
# Brandon Hall (HLLBRA005)
# 4 April 2014


def ndom_to_decimal(ndom): # This method converts ndom to decimal numbers, i.e base 6 to base 10
    
    decimal = ndom
    ndomS = str(ndom) # Converts the parsed number ndom to a string
    
    length = len(ndomS) # Length of the string is taken
    
    if(length == 2): # If its two numbers
        decimal = ( ( int(ndomS[0]) * 6 )  + int(ndomS[1]) )
        
    if (length == 3): # If its three numbers
        nd = ( ( int(ndomS[0]) * 6 )  + int(ndomS[1]) )
        decimal = (nd*6)  + int(ndomS[2]) 
        
    return decimal

def decimal_to_ndom(decimal): 
    
    
    power = 0
    multiple = decimal
    re  = ""
    ans = 0
    while (multiple >=1):
        
        re += str((multiple)%6) #remainder                
        multiple = multiple//6 #base number
        

        
       
    return int(re[::-1])

def ndom_add(a,b):  # converts to decimal, adds two  numbers 
                      # it then converts them into ndom numbers
    
    decA = ndom_to_decimal(a) 
    
    decB = ndom_to_decimal(b)
    
    dec = decA+decB
    ndom_tot = decimal_to_ndom(dec)
    
    return ndom_tot
    
def ndom_multiply(a,b): # This method multiplies two ndom numbers
                           # It does this by multipying the numbers and then
                           # converting them to ndom
    
  
    A = ndom_to_decimal(a) 
    B = ndom_to_decimal(b)
    dec = A*B
    ndom_tot = decimal_to_ndom(dec)    
    
    return ndom_tot