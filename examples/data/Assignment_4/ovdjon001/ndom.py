""" Assignment 4 Questiosn 2 by Jonathan Ovadia
on the 31st of Marth 2014"""

def ndom_to_decimal (a):
    a  = str(a)
    hundreds = 0
    tens = 0 
    units = 0
    if len(a) == 3:
        hundreds = eval(a[0])
        tens = eval(a[1])
        units =eval(a[2])
    elif len(a) == 2:
        tens = eval(a[0])
        units =eval(a[1] )       
    else:
        units = a
    num = (((hundreds*6)+tens)*6) + units
    return num



def decimal_to_ndom (a):
    units = a%6
    tens = (a//6)%6
    hundreds = (a//6//6)%6
    num = ""
    if hundreds != 0 :
        num +=str(hundreds)
    if tens!= 0 or hundreds !=0:
        num+=str(tens)

    num+=str(units)
    return num

def ndom_add (a, b):
    return (decimal_to_ndom (ndom_to_decimal (a)+ndom_to_decimal (b)))

def ndom_multiply (a, b):
    return (decimal_to_ndom (ndom_to_decimal (a)*ndom_to_decimal (b)))   
