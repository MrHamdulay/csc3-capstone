
def ndom_to_decimal(a):
    
    second = 0
    third = 0
    
    a = str(a)
    
    first = eval(str(a[0]))
    
    if len(a) == 2 :
        first = eval(str(a[1]))
        second = eval(str(a[0]))

    if len(a) == 3 :
        first = eval(str(a[2]))
        second = eval(str(a[1]))
        third = eval(str(a[0]))

    dec = first + (second * 6) + (third * 6**2)
    
 
    return dec

def decimal_to_ndom(a):

    ndom = 0
    if(a < 6) :
        ndom = a

    if(6 <= a < 36) :
        ndom = ((a%6)) + a//6 * 10

    if( a >= 36) :
        ndom = (a%6) + ((a//6)%6 * 10) + (a//36) * 100

    return ndom

def ndom_add(a, b) :

    return decimal_to_ndom((ndom_to_decimal(a)) + (ndom_to_decimal(b)))

def ndom_multiply(a, b) :

    return decimal_to_ndom((ndom_to_decimal(a)) * (ndom_to_decimal(b)))
