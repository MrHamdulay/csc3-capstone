#Ailsa Mackay: MCKAIL001
#2014-04-01
#Assignment4 Q2: ndom

def decimal_to_ndom(d):
    c=d%6
    b=(d//6)%6
    a=((d//6)//6)%6
    if c==0 and b==0:
        return str(a)
    elif c==0:
        return str(b)+str(a)
    else:
        return str(c)+str(b)+str(a)

def add_ndom(x,y):
    newx=ndom_to_decimal(a)
    newy=ndom_to_decimal(b)
    sum1=a+b
    result=ndom_to_decimal(sum1)
    return result
def ndom_to_decimal(a):
    hundreds=a//100
    tens=(a%100)//10
    units=(a%100)%10
    return (hundreds*(6**2)+tens*(6**1)+units*(6**0))

def ndom_add(a, b):
    hundreds=a//100
    tens=(a%100)//10
    units=(a%100)%10
    A=(hundreds*(6**2)+tens*(6**1)+units*(6**0))
    
    hundreds=b//100
    tens=(b%100)//10
    units=(b%100)%10
    B=(hundreds*(6**2)+tens*(6**1)+units*(6**0))
    
    C=A+B
    units=C//6
    ndom_units=C%6
    tens=units//6
    ndom_tens=units%6
    hundreds=tens//6
    ndom_hundreds=tens%6
    thousands=hundreds//6
    ndom_thousands=hundreds%6
    
    if ndom_thousands==0 and ndom_hundreds==0:
        return (str(ndom_tens)+str(ndom_units))
    elif ndom_thousands==0:
        return (str(ndom_hundreds)+str(ndom_tens)+str(ndom_units))   
    else: 
        return (str(ndom_thousands)+str(ndom_hundreds)+str(ndom_tens)+str(ndom_units))    

def ndom_multiply(a,b):
#converting from ndom to decimal    
    hundreds=a//100
    tens=(a%100)//10
    units=(a%100)%10
    A=(hundreds*(6**2)+tens*(6**1)+units*(6**0))
    
    hundreds=b//100
    tens=(b%100)//10
    units=(b%100)%10
    B=(hundreds*(6**2)+tens*(6**1)+units*(6**0)) 
#multiplying decimals
    C=A*B
#converting back to ndom and printing
    units=C//6
    ndom_units=C%6
    tens=units//6
    ndom_tens=units%6
    hundreds=tens//6
    ndom_hundreds=tens%6
    thousands=hundreds//6
    ndom_thousands=hundreds%6
    if ndom_thousands==0 and ndom_hundreds==0:
        return(str(ndom_tens)+str(ndom_units))
    elif ndom_thousands==0:
        return(str(ndom_hundreds)+str(ndom_tens)+str(ndom_units))
    else:
        return(str(ndom_thousands)+str(ndom_hundreds)+str(ndom_tens)+str(ndom_units))    