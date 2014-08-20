"""Christopher Sterley
01/04/2014
Computer science assignment"""

def ndom_to_decimal (choice):
    """function to convert from Ndom* to decimals"""
    choice=str(choice)
    if len(choice)==3:
        return 36*eval(choice[0])+6*eval(choice[1])+eval(choice[2])
    if len(choice)==2:
        return 6*eval(choice[0])+eval(choice[1])
    else:
        if eval(choice)<=5:
            return eval(choice)
        else:
            return eval(choice)+4
            
def decimal_to_ndom (a):
    """function to convert from decimals to Ndom*"""
    a=str(a)
    if int(a)>=36:
        dec=((eval(a)//36)*100)+(eval(a)%36//6*10)+((eval(a)%36)%6)
        return dec
    elif int(a)>5:
        dec=(eval(a)//6)*10+(eval(a)%6)
        return dec
    else:
        return eval(a)
        
    
def ndom_add (a, b):
    """Function to add two Ndom* numbers via convestion to decimal"""
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    c=x+y
    c=str(c)
    final=decimal_to_ndom(c)
    return final

def ndom_multiply (a, b):
    """function to multiply two Ndom* numbers via conversion to decimal"""
    x=ndom_to_decimal(a)
    y=ndom_to_decimal(b)
    c=(x*y)
    c=str(c)
    final=decimal_to_ndom(c)
    return final