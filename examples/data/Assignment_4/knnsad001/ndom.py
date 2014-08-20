def decimal_to_ndom(a):
    if a<6:
        return(a)
    if 6<=a<10:
        print(int((6*(a//6)*(5/3))+(a-(a//6)*6)))
    if 10<=a<100:
        hundreds=(a//36)
        tens=((a%36)//6)
        units=((a%36)%6)
        if hundreds==0:
            return(str(str(tens)+str(units)))
        else:
            return(str(hundreds)+str(tens)+str(units))
    if 100<=a<1000:
        thousands=(a//216)
        hundreds=((a%216)//36)
        tens=(((a%216)%36)//6)
        units=((a%216)%36)%6
        if thousands==0:
            return(str(hundreds)+str(tens)+str(units))
        else: 
            return(str(thousands)+str(hundreds)+str(tens)+str(units))

def ndom_to_decimal(a):
    hundreds=(a//100)*(6**2)
    tens=((a%100)//10)*(6**1)
    units=((a%100)%10)*(6**0)
    return(hundreds+tens+units)
    
def ndom_add(a,b):

    hundreds=(a//100)*(6**2)
    tens=((a%100)//10)*(6**1)
    units=((a%100)%10)*(6**0)
    A=(hundreds+tens+units)
    
    hundreds=(b//100)*(6**2)
    tens=((b%100)//10)*(6**1)
    units=((b%100)%10)*(6**0)
    B=(hundreds+tens+units)    
    
    z=A+B
    units=z//6
    ndom_units=z%6
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
        
def ndom_multiply(a,b):
    hundreds=(a//100)*(6**2)
    tens=((a%100)//10)*(6**1)
    units=((a%100)%10)*(6**0)
    A=(hundreds+tens+units)    
    
    hundreds=(b//100)*(6**2)
    tens=((b%100)//10)*(6**1)
    units=((b%100)%10)*(6**0)
    B=(hundreds+tens+units) 
    
    C=A*B
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
        return(str(ndom_hundreds)+ str(ndom_tens) +str(ndom_units))
    else:
        return(str(ndom_thousands)+str(ndom_hundreds)+str(ndom_tens)+str(ndom_units))    
    
    
    
    
    