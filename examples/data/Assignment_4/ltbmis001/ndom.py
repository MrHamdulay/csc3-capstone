import math

def ndom_to_decimal(a):
    b=str(a)
    if len(b)==1:
        num=a
    if len(b)==2:
        num=(eval(b[0:1])*6+eval(b[1:2]))
    if len(b)==3:
        num=(eval(b[0:1])*36+eval(b[1:2])*6+eval(b[2:3]))
    return(num)
    
def decimal_to_ndom(a):
    l =[]
    num= ""
    while a > 0:
        l.append(a % 6)
        a = math.floor(a/6)
    for x in range(len(l)):
        num = str(l.pop(0))+num
    return (eval(num))   
 
        
def ndom_add (a,b):
    x=ndom_to_decimal(a)+ndom_to_decimal(b)
    num=decimal_to_ndom (x)
    return(num)

def ndom_multiply (a, b):
    x=ndom_to_decimal(a)*ndom_to_decimal(b)
    num=decimal_to_ndom (x)
    return(num)


    