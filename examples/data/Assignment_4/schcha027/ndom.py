def ndom_to_decimal(number):
    number=str(number)
    length=len(number)
    if length==3:
        x=eval(number[0])*36
        y=eval(number[1])*6
        z=eval(number[2])
        tot=(x+y+z)
        return(tot)
    elif length==2:
        y=eval(number[0])*6
        z=eval(number[1])
        tot=(y+z)        
        return(tot)  
    elif length==1:
        z=eval(number[0])
        tot=(z)
        return(tot)
    #--------------------------------------------------------
def decimal_to_ndom (number):
    
    number= str(number)
    length=len(number)
    x=number
    if 0<length<4:
        s1,s2,s3=eval(x)//36, eval(x)%36//6, eval(x)%36%6
        if(s1==0):
            zz=str(s2)+str(s3)
        elif(s1==s2==0):
            zz=str(s3)
        else:
            zz=str(s1)+str(s2)+str(s3)
        return(zz)           
  #--------------------------------------------------------   
def ndom_add(number1,number2):
    num1=(ndom_to_decimal(number1))
    num2=(ndom_to_decimal(number2))
    number3=(num1)+(num2)
    num3=decimal_to_ndom (number3)
    return (num3)
 #--------------------------------------------------------
def ndom_multiply(number1,number2):
    num1=(ndom_to_decimal(number1))
    num2=(ndom_to_decimal(number2))
    
    number3=(num1*num2)
        
    num3= decimal_to_ndom(number3)
    return (num3)
 #--------------------------------------------------------
    