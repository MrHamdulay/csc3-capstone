'''ndom converter
Author:Raees Eland
01 April 2014'''

'''converts base 6 numbers to base 10 numbers'''
def ndom_to_decimal (a):    
    a=str(a)
    r=int(a[0])
    w=1
    while w!=len(a):
        r=r*6+int(a[w])
        w+=1
    return r

'''converts base 10 numbers to base 6 numbers'''   
def decimal_to_ndom (a):
    a=str(a)
    x,y=int(a),int(a)
    t,z=0,0
    for i in range(len(a)+1):
        y=str(x%6)
        x=x//6
        z+=int(y)*(10**(len(a)-len(a)+t))
        t+=1
    return z

'''Adds base 6 numbers'''
def ndom_add(a,b):
    a=ndom_to_decimal (a)
    b=ndom_to_decimal (b)
    c=a+b
    c=decimal_to_ndom(c)
    return c

'''Multiplies base 6 numbers'''
def ndom_multiply(a,b):
    a=ndom_to_decimal (a)
    b=ndom_to_decimal (b)
    c=a*b
    c=decimal_to_ndom (c)
    return c    
    


     

         
    
        
        
    
        
    

               