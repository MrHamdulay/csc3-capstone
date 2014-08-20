#WXXYUA004 Yuan-Yow Wu 04-02-2014
#Mathematical functions map naturally to program functions and modules often
#are used to group such functions for reuse.

def ndom_to_decimal (a): #function that converts a Ndom number to decimal.
    if a<=5: #this is for single ndom numbers
        return a 
        
    elif 10<=a<=50: #this is for double ndom numbers
        x=str(a)[1]
        y=str(a)[0] #we have got the double digit of the ndom number.
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
        
        final=ndom[::-1]
    return final
    
  
def ndom_add(a, b):        
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x+y
    final=decimal_to_ndom(z)
    return final

def ndom_multiply(a, b):
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    z=x*y
    final=decimal_to_ndom(z)
    return final