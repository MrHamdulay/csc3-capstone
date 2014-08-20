def decimal_to_ndom(a):
    return((a//36)*40+((a//6)*4)+a)

def ndom_to_decimal(a):
    return(a-4*(a//10)-(a//100)*24)

def ndom_add(a,b):
    c=(a-4*(a//10)-(a//100)*24)+(b-4*(b//10)-(b//100)*24)
    return((c//36)*40+((c//6)*4)+c)

def ndom_multiply(a,b):
    c=(a-4*(a//10)-(a//100)*24)*(b-4*(b//10)-(b//100)*24)
    return((c//36)*40+((c//6)*4)+c)