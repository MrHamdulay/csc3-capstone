
def ndom_to_decimal (a):
    num = 0
    aSt = str(a)
    exponent = len(aSt)
    for i in aSt:
        exponent -= 1
        i = int(i)
        num = num + i*(6**exponent)      
    return num
        
def decimal_to_ndom (a):
    quotient = a
    total = ""
    while quotient != 0:
        remainder = quotient % 6
        quotient//=6
        remainderST = str(remainder)
        total+= remainderST
       
    return total[::-1]     

def ndom_add (a,b):

    ta=0
    a=str(a)
    exp=len(a)
    for x in a:
        exp=exp-1
        x=int(x)
        ta = ta + (x*(6**exp))
            
    tb=0
    b=str(b)
    exp=len(b)
    for x in b:
        exp=exp-1
        x=int(x)
        tb = tb + (x*(6**exp))
        
    t = ta + tb
       
    quotient = t
    new =""
    while quotient !=0:
        remainder = quotient%6
        quotient =quotient//6
        remainderST=str(remainder)
        new += remainderST
    return new[::-1]

def ndom_multiply (a, b):
    
    ta=0
    a=str(a)
    exponent=len(a)
    for x in a:
        exponent=exponent-1
        x=int(x)
        ta +=(x*(6**exponent))
            
    tb=0
    b=str(b)
    exponent=len(b)
    for x in b:
        exponent=exponent-1
        x=int(x)
        tb +=(x*(6**exponent))
        
    total = ta *tb
       
    quotient =total
    new=""
    while quotient !=0:
        remainder = quotient%6
        quotient =quotient//6
        remainderST=str(remainder)
        new+= remainderST
    return new[::-1]        