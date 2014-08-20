''' Assignment 4 question 2
Tristan Subroyen '''

def ndom_to_decimal (a):
    '''converts a Ndom number to decimal'''
    # Initializations:
    final = 0 # initializes final
    length = len(str(a)) # determines length of string a
    string = str(a) # assigns string to string a ---> LAZY
    if (length == 2): # if a is 2 digits long...
        if (string[1] == '0'): # if a is a multiple of 10... Note: this may be irrelevant... poor coding :/
            final = final+((eval(string[0]))*6) # calculate final
        else: # if a is not a perfect multiple of 10...
            final = final+((eval(string[0]))*6)+((eval(string[1]))*1) 
    elif (length == 1): # if a is one digit long
        if (a!=6) and (a!=7) and (a!=8) and (a!=9):
            final = final+a
        else:
            error = 'error'
            return error
    elif (length == 3): # if a is 3 digits long...
        final = final+((eval(string[0]))*36)+((eval(string[1]))*6)+((eval(string[2]))*1)      
    return final # return the value final

def decimal_to_ndom (a):
    digits = '0123456789'
    s = ''
    while 1:
        r = a % 6
        s = digits[r] + s
        a = a // 6
        if a == 0:
            break
    final = eval(s)
    return final        
    
def ndom_add (a, b):
    final = 0
    num1 = ndom_to_decimal (a)
    num2 = ndom_to_decimal (b)
    sumNum = num1 + num2
    final = final+(decimal_to_ndom (sumNum))
    return final
        
def ndom_multiply (a, b):
    final = 0
    mult1  = ndom_to_decimal (a)
    mult2 = ndom_to_decimal (b)
    mult3 = mult1*mult2
    final = final+(decimal_to_ndom (mult3))
    return final
    
    
    

        
            
        
        
        
        
        
        
    

        
    
            
        
        
        
        