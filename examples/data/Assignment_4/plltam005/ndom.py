def ndom_to_decimal (a):
    number=(a//100)*36+(a%100//10)*6+a%10
    return number
 
def decimal_to_ndom (a):
    hundreds=a//36
    tens=(a%36)//6
    units=a%6
    if hundreds == 0:
        hundreds=""
    if tens==0 and hundreds==0:
        tens=""    
    jack=eval(str(hundreds)+str(tens)+str(units)) 
    return (jack)

def ndom_add (a, b):
    x=ndom_to_decimal (a)+ndom_to_decimal (b)
    l=decimal_to_ndom (x)
    return (l)

def ndom_multiply (a, b):
    x=ndom_to_decimal (a)*ndom_to_decimal (b)
    k=decimal_to_ndom(x)
    return (k)