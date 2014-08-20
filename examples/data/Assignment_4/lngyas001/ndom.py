def ndom_to_decimal (a):#that converts a Ndom number to decimal
    dec = 0
    exp = 0
    while a != 0:
        dec+= a%10*6**exp
        a = a//10
        exp+=1
    return dec

def decimal_to_ndom (a):#that converts a decimal number to Ndom
    x = ''
    while True:
        x = str(a%6) + x
        a = a//6
        if (a == 0):
            break
       
    return x   
    
        

def ndom_add (a, b):     #that adds 2 Ndom numbers
    new_a = ndom_to_decimal(a)
    new_b = ndom_to_decimal(b)
    c = new_a + new_b
    new_c = decimal_to_ndom(c)
    return new_c

def ndom_multiply (a, b):#that multiples 2 Ndom numbers
    new_a = ndom_to_decimal(a)
    new_b = ndom_to_decimal(b)
    c = new_a * new_b
    new_c = decimal_to_ndom(c)
    return new_c
    

