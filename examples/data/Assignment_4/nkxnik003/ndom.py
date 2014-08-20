#Nikhil Jiten Naik
#NKXNIK003

def decimal_to_ndom(a):
    if a<6:
        return(a)
    if 6<=a<10:
        print(int((6*(a//6)*(5/3))+(a-(a//6)*6)))
    if 10<=a<100:
        hund=(a//36)
        ten=((a%36)//6)
        uni=((a%36)%6)
        if hund==0:
            return(str(str(ten)+str(uni)))
        else:
            return(str(hund)+str(ten)+str(uni))
    if 100<=a<1000:
        thous=(a//216)
        hund=((a%216)//36)
        ten=(((a%216)%36)//6)
        uni=((a%216)%36)%6
        if thous==0:
            return(str(hund)+str(ten)+str(uni))
        else: 
            return(str(thous)+str(hund)+str(ten)+str(uni))

def ndom_to_decimal(a):
    hund=(a//100)*(6**2)
    ten=((a%100)//10)*(6**1)
    uni=((a%100)%10)*(6**0)
    return(hund+ten+uni)
    
def ndom_add(a,b):

    hund=(a//100)*(6**2)
    ten=((a%100)//10)*(6**1)
    uni=((a%100)%10)*(6**0)
    A=(hund+ten+uni)
    
    hund=(b//100)*(6**2)
    ten=((b%100)//10)*(6**1)
    uni=((b%100)%10)*(6**0)
    B=(hund+ten+uni)    
    
    z=A+B
    uni=z//6
    ndom_uni=z%6
    ten=uni//6
    ndom_ten=uni%6
    hund=ten//6
    ndom_hund=ten%6
    thous=hund//6
    ndom_thous=hund%6
    if ndom_thous==0 and ndom_hund==0:
        return(str(ndom_ten)+str(ndom_uni))
    elif ndom_thous==0:
        return(str(ndom_hund)+str(ndom_ten)+str(ndom_uni))
    else:
        return(str(ndom_thous)+str(ndom_hund)+str(ndom_ten)+str(ndom_uni))
        
def ndom_multiply(a,b):
    hund=(a//100)*(6**2)
    ten=((a%100)//10)*(6**1)
    uni=((a%100)%10)*(6**0)
    A=(hund+ten+uni)    
    
    hund=(b//100)*(6**2)
    ten=((b%100)//10)*(6**1)
    uni=((b%100)%10)*(6**0)
    B=(hund+ten+uni) 
    
    C=A*B
    uni=C//6
    ndom_uni=C%6
    ten=uni//6
    ndom_ten=uni%6
    hund=ten//6
    ndom_hund=ten%6
    thous=hund//6
    ndom_thous=hund%6
    if ndom_thous==0 and ndom_hund==0:
        return(str(ndom_ten)+str(ndom_uni))
    elif ndom_thous==0:
        return(str(ndom_hund)+ str(ndom_ten) +str(ndom_uni))
    else:
        return(str(ndom_thous)+str(ndom_hund)+str(ndom_ten)+str(ndom_uni))    
    
    
    
    
    