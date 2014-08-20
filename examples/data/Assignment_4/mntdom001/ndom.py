# ndom.py
# Dominic Manthoko
# 03 April 2014

def decimal_to_ndom(a):
    """ this function converts decimal number into a ndom number"""
    num = a
    denom = 6                                                                   #  the denominator is constant
    ndom_string = ""                                                            #  create a string called num_string where all the remainders will be stored
    
    con = True
    
    while con:
        if num>=denom:                                                          # the body will execute only if the numerator is greater than the denominator
            ndom_string += str(num%denom)                                       # add the remainder to ndom_string
            num = num//denom                                                    # the next numerator is equal to the previous numerator divided by the constant denominator
            
        else:
            ndom_string += str(num)                                             # when the denominator is greater than the numerator, append that numerator to ndom_string
            con = False                                                         # set con to false so that the loop will not run
            
    return int(ndom_string[::-1])                                               # return the interger value of ndom_string in reverse

def ndom_to_decimal(a):
    """this function converts ndom number to decimal"""
    
    ndom = str(a)
    ndom = ndom[::-1]
    decimal = 0
    exp = 0
    
    for c in ndom:
        num = int(c)
        decimal += (num * (6**exp))
        exp +=1
        
    return decimal
    
    
def ndom_add(a,b):
    """ this function adds to ndom numbers"""
    
    add = ndom_to_decimal(a) + ndom_to_decimal(b)
    ans = decimal_to_ndom(add)
    return ans

def ndom_multiply(a,b):
    """this function multiplies two ndom numbers"""
    
    muliply = ndom_to_decimal(a) * ndom_to_decimal(b)
    ans = decimal_to_ndom(muliply)
    return ans
