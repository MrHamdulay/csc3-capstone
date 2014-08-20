#Aidan de Nobrega
#Functions for converting between senary and decimal
#31/03/2014

def ndom_to_decimal(a):
    a = str(a) #iot index
    decimal = int(a[0])
    for i in a[1:]:
        decimal *= 6
        decimal += int(i)
    return decimal
    
def decimal_to_ndom(a):
    units = a % 6
    tens = (a//6) % 6
    hundreds = (a//36) % 6
    senary = units + tens*10 + hundreds*100
    return senary    
    
def ndom_add(a, b):
    A = ndom_to_decimal(a)
    B = ndom_to_decimal(b) #converts both to decimal
    decimal_answer = A + B #adds decimal values
    ndom_answer = decimal_to_ndom(decimal_answer) #converts to senary
    return ndom_answer

def ndom_multiply(a, b):
    A = ndom_to_decimal(a)
    B = ndom_to_decimal(b) #same concept as ndom_add(a, b)
    decimal_answer = A * B
    ndom_answer = decimal_to_ndom(decimal_answer)
    return ndom_answer