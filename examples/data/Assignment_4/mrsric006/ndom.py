
import math                    

def ndom_to_decimal(a):                #ndom to decimal conversion
    value = 0
    for i in range(0, len(str(a))):                        
        value += int(str(a)[i])*(6**(len(str(a))-i-1))           #changing away from base 6
    return value

def decimal_to_ndom(a):
    output = 0
    for i in range (10, -1, -1):
        output += (a//(6**i))*10**i                    #converting into base 6
        a = a % (6**i)
    return output
        
def ndom_add (a, b):
    return decimal_to_ndom(ndom_to_decimal(a) + ndom_to_decimal(b))            #using previous functions add

def ndom_multiply (a, b):
    return decimal_to_ndom(ndom_to_decimal(a) * ndom_to_decimal(b))
        
 