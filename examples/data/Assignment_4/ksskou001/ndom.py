#Name: Kouame KOUASSI
#Student_Number: KSSKOU001
#Date: 29-03-2014
#Assignment_4
#Question2_ndom or base 6 = 'string' and def functions():

def ndom_to_decimal(a):
    
    ''' This function convert numbers of base 6 to numbers of base 10'''
    
    a_str=str(a)
    if 0<= a <=5: a=a

    else:
        c, a_new = 0 , 0
        for i in range(len(a_str)-1,-1,-1):
            
            a_new+=int(a_str[i])*pow(6,c)
            c+=1
            a=a_new
    return a 

def decimal_to_ndom(a):
    
    ''' This function convert numbers of base 10 to numbers of base 6'''
        
    if 0 <= a <= 5: a = a 
    
    elif 6 <= a <= 35:
        
        a = str(a//6) + str(a%6)
    else:
        digit1 = str(a//36)
        digit2 = str((a%36)//6)
        digit3 = str((a%36)%6)
        a_new = digit1 + digit2 + digit3
        a = int(a_new)
    return int(a)


def ndom_add(a,b):
    
    '''This function returns the sum of two numbers of base 6'''
    
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)     
    
    return decimal_to_ndom(a+b)

def ndom_multiply(a,b):
    
    '''This function returns the product of two numbers of base 6'''
    
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    
    return decimal_to_ndom(a*b)    