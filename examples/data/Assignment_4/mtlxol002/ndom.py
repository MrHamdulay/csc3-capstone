#Xola Matlanyane
#4 April 2014
#CSC1015F Assignment 4 Q2


def ndom_to_decimal(a):
    x=str(a)
    
    if len(x)== 1:
        number1= int(x[:1])
        return number1*6
    elif len(x)== 2:
        numnber1= int(x[:1])
        number2= int(x[1:2])
        return (number1*6)+number2
    elif len(x)== 3:
        number1= int(x[:1])
        number2= int(x[1:2])        
        number3= int(x[2:3])
        return ((((number*6)+number2)*6)+number3)
        
def decimal_to_ndom(a):
    x=str(a)
    
    if len(x)==1:
        number1= int(x)
        return (number1/6)*10        
    elif len(x)== 2:
        y= int(x)
        number2rem1= y%6
        number2= int(y//6)
        number2rem2= number2%6
        number3= int(number2//6)
        number3rem3= number3%6
        if number3rem3==0:
            z= str(number2rem2)+str(number2rem1)
            return eval(z)
        else:
            z=str(number3rem3)+str(number2rem2)+str(number2rem1)
            return eval(z)
    elif len(x)== 3:
        y= int(x)
        number2rem1= y%6
        number2= int(y//6)
        number2rem2= number2%6
        number3= int(number2//6)
        number3rem3= number3%6
        z=str(number3rem3)+str(number2rem2)+str(number2rem1)
        return eval(z)
        
def ndom_add(a,b):
    x= ndom_to_decimal(a)
    y= ndom_to_decimal(b)
    z= x+y
    return decimal_to_ndom(z)
    
def ndom_multiply(a,b):
    x= ndom_to_decimal(a)
    y= ndom_to_decimal(b)
    z= x*y
    return decimal_to_ndom(z)