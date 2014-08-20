"""
Prashanth Sridharan
SRDPRA001
Assignment 4
ndom
"""
def ndom_to_decimal(a):
    a=str(a)
    if(len(a)==3):
        total = (((((eval(a[0]))*6)+(eval(a[1])))*6)+eval(a[2]))
    elif(len(a)==2):
        total=((eval(a[0])*6)+eval(a[1]))
    else:
        total=a
    return total
    
def decimal_to_ndom(a):
    string=str(a)
    if(len(string)==1):
        total=a
    else:
        quot=a//6
        total=str(a%6)
        while(quot>=1):
            total=str(quot%6)+total
            quot=quot//6  
        return total
        
def ndom_add(a,b):
    return eval(decimal_to_ndom((ndom_to_decimal(a))+(ndom_to_decimal(b))))
    
def ndom_multiply(a,b):
    return eval(decimal_to_ndom((ndom_to_decimal(a))*(ndom_to_decimal(b))))