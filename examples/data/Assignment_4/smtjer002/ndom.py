"""A program to convert Ndom to Decimal and back, and to add and multiply Ndom numbers
By Jeremy Smith SMTJER002
31 March 2014"""

def decimal_to_ndom(a):
    """converts an ndom number to decimal"""
    place3 = a//36
    decimal=place3*100
    a-=(place3*36)
    place2 = a//6
    decimal+=place2*10
    a-=(place2*6)
    place1 = a*1
    decimal+=place1*1
    
    return decimal

def ndom_to_decimal(a):
    """converts a decimal number to ndom"""
    place3 = a//100
    decimal=place3*36
    a-=(place3*100)
    place2 = a//10
    decimal+=place2*6
    a-=(place2*10)
    place1 = a*1
    decimal+=place1*1
    
    return decimal

def ndom_add(a,b):
    """calculates the addition of two ndom numbers"""
    num1=ndom_to_decimal(a)
    num2=ndom_to_decimal(b)
    ans=num1+num2
    ans=decimal_to_ndom(ans)
    
    return ans

def ndom_multiply(a,b):
    """calculates the multiplication of two ndom numbers"""
    num1=ndom_to_decimal(a)
    num2=ndom_to_decimal(b)
    ans=num1*num2
    ans=decimal_to_ndom(ans)
    
    return ans

#x=ndom_to_decimal(12)
#print(x)

#z=ndom_multiply(13,14)
#print(z)

#a=decimal_to_ndom(20)
#print(a)

#y=ndom_add(123,141)
#print(y)