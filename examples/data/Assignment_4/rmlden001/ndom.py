#Denisha
#Student number: RMLDEN001
#04/04/2014



def ndom_to_decimal(a):
    x=str(a)
    
    if len(x)== 1:
        num1= int(x[:1])
        return num1*6
    elif len(x)== 2:
        num1= int(x[:1])
        num2= int(x[1:2])
        return (num1*6)+num2
    elif len(x)== 3:
        num1= int(x[:1])
        num2= int(x[1:2])        
        num3= int(x[2:3])
        return ((((num1*6)+num2)*6)+num3)
        
def decimal_to_ndom(a):
    x=str(a)
    
    if len(x)==1:
        num1= int(x)
        return (num1/6)*10        
    elif len(x)== 2:
        y= int(x)
        num2rem1= y%6
        num2= int(y//6)
        num2rem2= num2%6
        num3= int(num2//6)
        num3rem3= num3%6
        if num3rem3==0:
            z= str(num2rem2)+str(num2rem1)
            return eval(z)
        else:
            z=str(num3rem3)+str(num2rem2)+str(num2rem1)
            return eval(z)
    elif len(x)== 3:
        y= int(x)
        num2rem1= y%6
        num2= int(y//6)
        num2rem2= num2%6
        num3= int(num2//6)
        num3rem3= num3%6
        z=str(num3rem3)+str(num2rem2)+str(num2rem1)
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