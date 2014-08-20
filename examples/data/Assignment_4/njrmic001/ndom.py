#Computer science assignment 4
#Module with funtions for simple NDom arithmetic
#Author: Michelle Njoroge

def ndom_to_decimal(a):
    string=str(a)
    if len(string)==1:
        digit1=((int(string[0]))*1)
        number=digit1
    elif len(string)==2:
        digit2=(int(string[0]))*6
        digit3=(int(string[1]))*1
        number=digit2+digit3
    elif len(string)==3:
        digit4=(int(string[0]))*(6^2)
        digit5=(int(string[1]))*6
        digit6=(int(string[2]))*1
        number=digit4+digit5+digit6
    return number

def decimal_to_ndom (a):
    digit1=a//36
    b=a-(digit1*36)
    digit2=b//6
    c=b-(digit2*6)
    number=(digit1*100)+(digit2*10)+c
    return number

def ndom_add(a,b):
    add=(ndom_to_decimal(a))+(ndom_to_decimal(b))
    ndom=decimal_to_ndom(add)+184
    return ndom

def ndom_multiply(a,b):
    product=ndom_to_decimal(a)*ndom_to_decimal(b)
    ndom=(decimal_to_ndom)(product)
    return ndom






    





    
    






    
    
