'''
Created on 02 Apr 2014

@author: Yusuf
'''
def ndom_to_decimal (a): #that converts a Ndom number to decimal
    a = 1000 + a
    a = str(a)
    a,b,c = eval(a[1]),eval(a[2]),eval(a[3])
    a = a*36
    a = a+(b*6)
    a = a+c
    return a
    
def decimal_to_ndom (a): #that converts a decimal number to Ndom
    q,w=0,0
    while (a-36)>=0:
        a=a-36
        q+=1
    while (a-6)>=0:
        a=a-6
        w+=1
    a = a + (w*10) + (q*100)
    return a
    
def ndom_add (a, b): #that adds 2 Ndom numbers
    c=ndom_to_decimal(a)+ndom_to_decimal(b)
    c=decimal_to_ndom (c)
    return c
    
def ndom_multiply (a, b): #that multiples 2 Ndom numbers
    a=ndom_to_decimal (a)
    b=ndom_to_decimal (b)
    a=a*b
    a=decimal_to_ndom (a)
    return a