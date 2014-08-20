#Ndom number ----> decimal.
def ndom_to_decimal (a): 
    if a<=5: 
        #single ndom numbers
        return a 
    #double ndom numbers
    elif 10<=a<=50: 
        x=str(a)[1]
        #2 digits of the ndom number.
        y=str(a)[0] 
        y=6*int(y)             
        a=int(x)+int(y)
        return a
    elif 100<=a<=500: #this is for triple ndom numbers
        x=str(a)[2]
        y=str(a)[1] #we have got the double digit of the ndom number.
        y=6*int(y)
        z=str(a)[0] #we have got the second digit of the ndom number.
        z=36*int(z)
        a=int(x)+int(y)+int(z)
        return a
        
def decimal_to_ndom (a):

    ndom=""
    wholenumber=a
    
    while wholenumber>0:
        rem=wholenumber%6
        wholenumber=wholenumber//6
        ndom=ndom+str(rem)
        
        end=ndom[::-1]
    return end
    
  
def ndom_add(a, b):        
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x+y
    end=decimal_to_ndom(z)
    return end

def ndom_multiply(a, b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x*y
    end=decimal_to_ndom(z)
    return end