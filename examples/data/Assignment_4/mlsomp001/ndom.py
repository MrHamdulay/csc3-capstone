# Name: OMPHEMETSE
# Student no: MLSOMP001
# DATE: 04 APRIL 2014
# ASSIGNMENT RATING: TORTURE

def decimal_to_ndom(a):
    prott=(a//36)
    tang=((a-(36*prott))//6)
    num=(a%6)
    list=[prott,tang,num]
    string=str(list[0]) + str(list[1]) + str(list[2])
    string=int(string)
    return string

def ndom_to_decimal(a):
    a=str(a)
    if len(a)>1:
        tang=eval(a[-2])*6
    else:
        tang=0
    if len(a)>2:
        prott=eval(a[-3])*36
    else:
        prott=0
    num=eval(a[-1])
    num=prott+tang+num
    return num

def ndom_add(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    math=a+b
    math=decimal_to_ndom(math)
    return math

def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    math=a*b
    math=decimal_to_ndom(math)
    return math

