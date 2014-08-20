def ndom_to_decimal (a):
    stra = str(a)
    index = -1
    dec = 0
    for i in range(len(stra)):
        dec += int(stra[index])*(6**i)
        index -= 1
    return dec    
    
def decimal_to_ndom(a):
   
    rev_ndom = ""
    index = -1  
    div=a
    while True:
        if div < 6:
            rev_ndom += str(div)
            break
        rev_ndom += str(div%6)
        div = (div//6)
        
    return rev_ndom[::-1]

def ndom_add (a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a+b)

def ndom_multiply(a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    return decimal_to_ndom(a*b)