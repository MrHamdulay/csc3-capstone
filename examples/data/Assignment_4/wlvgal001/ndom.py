# Galya Wolov
#Ndom to Decimal and vice versa calculator
#1/4/2014

def ndom_to_decimal(a):
    num= str(a)
    if len(num)==3:
        b= num[2]
        c= num[1]
        d= num[0]
        e= eval(b) +eval(c) *6 +eval(d) *36 #first digit from right is left alone, second is *6, third * 6*6) asif 100 *100
        
    if len(num)==2:
        b= num[1]
        c= num[0]
        e= eval(b)+ eval(c)*6
    
    if len(num)==1:
        e= eval(num[0])
        
    return e




def decimal_to_ndom(a):
    num=''
    factor=a
    while factor!=0:
        factor=a//6
        num+=str(a%6)
        a=factor
    return str(num)[::-1]
def ndom_add(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))
def ndom_multiply(a,b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
    

    