def decimal_to_ndom(a):
    if a<6:
        return(a)
    if 6<=a<10:
        print(int((6*(a//6)*(5/3))+(a-(a//6)*6)))
    if 10<=a<100:
        digit_1=((a%36)%6)
        digit_2=((a%36)//6)
        digit_3=(a//36)
        if digit_3==0:
            return(str(str(digit_2)+str(digit_1)))
        else:
            return(str(digit_3)+str(digit_2)+str(digit_1))
    if 100<=a<1000:
        digit_4=(a//216)
        digit_3=((a%216)//36)
        digit_2=(((a%216)%36)//6)
        digit_1=((a%216)%36)%6
        if digit_4==0:
            return(str(digit_3)+str(digit_2)+str(digit_1))
        else: 
            return(str(digit_4)+str(digit_3)+str(digit_2)+str(digit_1))

def ndom_to_decimal(a):
    digit_3=(a//100)*(6**2)
    digit_2=((a%100)//10)*(6**1)
    digit_1=((a%100)%10)*(6**0)
    return(digit_3+digit_2+digit_1)
    
def ndom_add(a,b):

    digit_3=(a//100)*(6**2)
    digit_2=((a%100)//10)*(6**1)
    digit_1=((a%100)%10)*(6**0)
    a_=(digit_3+digit_2+digit_1)
    
    digit_3=(b//100)*(6**2)
    digit_2=((b%100)//10)*(6**1)
    digit_1=((b%100)%10)*(6**0)
    b_=(digit_3+digit_2+digit_1)    
    
    f=a_+b_
    digit_1=f//6
    ndom_digit_1=f%6
    digit_2=digit_1//6
    ndom_digit_2=digit_1%6
    digit_3=digit_2//6
    ndom_digit_3=digit_2%6
    digit_4=digit_3//6
    ndom_digit_4=digit_3%6
    if ndom_digit_4==0 and ndom_digit_3==0:
        return(str(ndom_digit_2)+str(ndom_digit_1))
    elif ndom_digit_4==0:
        return(str(ndom_digit_3)+str(ndom_digit_2)+str(ndom_digit_1))
    else:
        return(str(ndom_digit_4)+str(ndom_digit_3)+str(ndom_digit_2)+str(ndom_digit_1))
        
def ndom_multiply(a,b):
    digit_3=(a//100)*(6**2)
    digit_2=((a%100)//10)*(6**1)
    digit_1=((a%100)%10)*(6**0)
    a_=(digit_3+digit_2+digit_1)    
    
    digit_3=(b//100)*(6**2)
    digit_2=((b%100)//10)*(6**1)
    digit_1=((b%100)%10)*(6**0)
    b_=(digit_3+digit_2+digit_1) 
    
    d=a_*b_
    digit_1=d//6
    ndom_digit_1=d%6
    digit_2=digit_1//6
    ndom_digit_2=digit_1%6
    digit_3=digit_2//6
    ndom_digit_3=digit_2%6
    digit_4=digit_3//6
    ndom_digit_4=digit_3%6
    if ndom_digit_4==0 and ndom_digit_3==0:
        return(str(ndom_digit_2)+str(ndom_digit_1))
    elif ndom_digit_4==0:
        return(str(ndom_digit_3)+ str(ndom_digit_2) +str(ndom_digit_1))
    else:
        return(str(ndom_digit_4)+str(ndom_digit_3)+str(ndom_digit_2)+str(ndom_digit_1))    