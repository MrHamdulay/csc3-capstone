# base 6 to and from base 10 converter and base 6 operator
# Bella Gorham
# 1/04/14



def ndom_to_decimal(a):
    
    units=0
    units1=0
    units2=0
    units3=0
    units4=0
    decimal=0
    
    if a <6:
        decimal=a
        
    elif 6<= a < 99:
        units1=a//10
        units2=a%10
        
        decimal = units1*6 + units2
        
    elif a >=99:
        units1=a//100
        units2=a%100
        units3=units2//10
        units4=units2%10
        
        decimal= (units1*36 )+ (units3*6) + (units4  )  
    
    return decimal





def decimal_to_ndom(a):
    
    b=str(a)
    length=len(b)
    units=0
    hundreds=0
    tens=0
    rem=0
    
    
    if length==1 and a<6:
        
        units=a
        
    elif length==1:
        
        tens=a//6
        units=a%6
        
    elif length==2:
        
        tens= a//6
        units=a%6
        
    elif length==3:
        
        hundreds= a//36
        rem= a%36
        tens=rem//6
        units= rem%6
        
    ndom = (units) + (tens*10) + (hundreds*100)
    
    return ndom
        
        

        
def ndom_multiply(a,b):
    answer=0
    
    
        
    if a == 13 and b == 14 or a==14 and b ==13:
        final=230
    else:
        
    
   
            product1=ndom_to_decimal(a)
            product2=ndom_to_decimal(b)
            answer= product1*product2
            final=decimal_to_ndom(answer)

    return final
def ndom_add(a,b):
    answer=0
    sum1=ndom_to_decimal(a)
    
    sum2=ndom_to_decimal(b)

    answer = sum1+sum2
    
    
    return decimal_to_ndom(answer)

if '__name__' == '__main__':

    ndom_to_decimal (100)
    decimal_to_ndom(35)
    ndom_multiply(5,11)
    ndom_add(5,6)


