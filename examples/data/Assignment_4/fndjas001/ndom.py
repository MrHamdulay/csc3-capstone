"""A library containing functions that convert Ndom numbers to and from decimal
   as well as adding and multiplying 2 Ndom numbers
Jason Findlay
03/04/2014"""

"""A function to convert an Ndmom number to a decimal number"""
def  ndom_to_decimal(a):
    a=str(a)
    count=0
    b=0
    for i in a[::-1]:
        count+=1
        if count==1:
            b+=eval(i)
        elif count==2:
            b+=eval(i)*6
        elif count==3:
            b+=eval(i)*36
        else:
            print("The number can cantain a maximum of three digits")
    return(b)

"""A function that converts a decimal to Ndom"""
def decimal_to_ndom(a):
    b=""
    if a<6:
        b=a
    elif a<36:
        for i in range(2):
            b+=str(a%6)
            a//=6
    elif a<216:
        for i in range(3):
            b+=str(a%6)
            a//=6
    elif a<999:
        for i in range(4):
            b+=str(a%6)
            a//=6
    return(eval(b[::-1]))

"""A function that adds two Ndom numbers"""
def ndom_add(a,b):
    c=ndom_to_decimal(a)
    d=ndom_to_decimal(b)

    e=c+d

    f=decimal_to_ndom(e)
    return(f)

"""A function that multiplies two Ndom numbers"""
def ndom_multiply(a,b):
    c=ndom_to_decimal(a)
    d=ndom_to_decimal(b)

    e=c*d
    f=decimal_to_ndom(e)
    return(f)

    
