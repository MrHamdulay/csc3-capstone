
#bishum jahly!!!!!!!!!!!!!!!!!!!


def ndom_to_decimal(a):
    k=str(a)
    
    if len(k)== 1:
        num1= int(k[:1])   
        return num1*6
    elif len(k)== 2:
        num1= int(k[:1])
        num2= int(k[1:2])
        return (num1*6)+num2
    elif len(k)== 3:
        num1= int(k[:1])
        num2= int(k[1:2])        
        num3= int(k[2:3])
        return ((((num1*6)+num2)*6)+num3)
        

#go to hotseat to confirm


def decimal_to_ndom(a):
    k=str(a)
    
    if len(k)==1:
        num1= int(k)
        return (num1/6)*10        
    elif len(k)== 2:
        y= int(k)
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
    elif len(k)== 3:
        y= int(k)
        num2rem1= y%6
        num2= int(y//6)
        num2rem2= num2%6
        num3= int(num2//6)
        num3rem3= num3%6
        z=str(num3rem3)+str(num2rem2)+str(num2rem1)
        return eval(z)
        




def ndom_add(a,b):
    k= ndom_to_decimal(a)
    b= ndom_to_decimal(b)
    z= k+b
    return decimal_to_ndom(z)
    





def ndom_multiply(a,b):
    k= ndom_to_decimal(a)
    b= ndom_to_decimal(b)
    z= k*b
    return decimal_to_ndom(z)