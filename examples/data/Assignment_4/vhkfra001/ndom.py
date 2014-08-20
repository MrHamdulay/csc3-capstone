# Assignment 4
# Program to convert from base 10 to base 6 and vice versa; also + and x
# Frans van Hoek
# 3 March 2014

def decimal_to_ndom(a):
    power = 2
    ndoms = ""
    j = 0
    
    whole1 = str(a//36)
    rem1 = a%36
    ndoms += whole1
    
    whole2 = str(rem1//6)
    rem2 = rem1%6
    ndoms += whole2
    
    whole3 = str(rem2//1)
    rem3 = rem2%1
    ndoms += whole3
    
    if ndoms[0] == '0':
        ndoms = ndoms[1:]
        if ndoms[0] == '0':
            ndoms = ndoms[1]
    
    return ndoms

def ndom_to_decimal(a):
    ndoms = 0
    
    ndoms = int(str(a)[0])
    if len(str(a)) == 1: return ndoms
    
    ndoms = 6*ndoms
    ndoms += int(str(a)[1])
    if len(str(a)) == 2: return ndoms
    
    ndoms = 6*ndoms
    ndoms+= int(str(a)[2])
    return ndoms
    
def ndom_add (a, b):
    a = (str(a))[::-1]
    b = (str(b))[::-1]
    ndom = ""
    carry = 0
    c, d = 0, 0
    count = 0
    
    if len(a) >= len(b): 
        c = a
        d = b
    else: 
        c = b
        d = a
    
    for i in c:
        d += (len(c)-len(d))*"0"
        sum = int(i) + int(carry) + int((d)[count])      
        ndom += str(sum%6)
        carry = sum//6
        count += 1
    count = 0    
    ndom = (ndom+str(carry))[::-1]
    ndom = int(ndom)
    return ndom

def ndom_multiply(a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    
    product = a*b
    product = decimal_to_ndom(product)
    return int(product)

