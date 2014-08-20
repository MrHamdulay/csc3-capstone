

def decimal_to_ndom(a):

    numq = a
    denomq = 6                                                                   
    ndom_string = ""                                                            
    
    conq = True
    
    while conq:
        if numq>=denomq:                                                          
            ndom_string += str(numq%denomq)                                       
            numq = numq//denomq                                                   
            
        else:
            ndom_string += str(numq)                                             
            conq = False                                                         
            
    return int(ndom_string[::-1])                                               

def ndom_to_decimal(a):
    
    
    ndom = str(a)
    ndom = ndom[::-1]
    decimal = 0
    expq = 0
    
    for i in ndom:
        numq = int(i)
        decimal += (numq * (6**expq))
        expq +=1
        
    return decimal
    
    
def ndom_add(a,b):
    
    
    add = ndom_to_decimal(a) + ndom_to_decimal(b)
    ans = decimal_to_ndom(add)
    return ans

def ndom_multiply(a,b):
    
    
    muliply = ndom_to_decimal(a) * ndom_to_decimal(b)
    ans = decimal_to_ndom(muliply)
    return ans
