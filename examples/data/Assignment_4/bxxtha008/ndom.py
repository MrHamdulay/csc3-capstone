#Thabiso Beau
#01/04/2014
#Programme to convert ndom to decimal, decimal to ndom, add two ndoms and multiply two ndoms


def ndom_to_decimal(a):
    x=str(a)
    
    if len(x)== 1:
        no1= int(x[:1])
        return no1*6
    elif len(x)== 2:
        no1= int(x[:1])
        no2= int(x[1:2])
        return (no1*6)+no2
    elif len(x)== 3:
        no1= int(x[:1])
        no2= int(x[1:2])        
        no3= int(x[2:3])
        return ((((no*6)+no2)*6)+no3)
        
def decimal_to_ndom(a):
    x=str(a)
    
    if len(x)==1:
        no1= int(x)
        return (no1/6)*10        
    elif len(x)== 2:
        y= int(x)
        no2rem1= y%6
        no2= int(y//6)
        no2rem2= no2%6
        no3= int(no2//6)
        no3rem3= no3%6
        if no3rem3==0:
            z= str(no2rem2)+str(no2rem1)
            return eval(z)
        else:
            z=str(no3rem3)+str(no2rem2)+str(no2rem1)
            return eval(z)
    elif len(x)== 3:
        y= int(x)
        no2rem1= y%6
        no2= int(y//6)
        no2rem2= no2%6
        no3= int(no2//6)
        no3rem3= no3%6
        z=str(no3rem3)+str(no2rem2)+str(no2rem1)
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