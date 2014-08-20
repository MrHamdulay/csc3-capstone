def ndom_to_decimal (a):
    x100=(a//100)*36
    
    x10=((a%100)//10)*6
    
    x=a%10
    
    xtot=x100+x10+x

    return(xtot)
    
#ndom_to_decimal(1)

def decimal_to_ndom (a):
    x10=(a%36)//6
    
    x=a%6
    
    x100 = a//36
    
    if (x100 == 0):
       
        x100=""
        
    if (x10==0 and x100==0):
       
        x10=""
    
    n =str(x100)+str(x10)+str(x)
   
    #n = x100+x10+x
    
    #n1=str(n)
    
    n1=eval(n)
    
    return n1  
    
    #a=int(input("just type it"))
    #ndom_36,rem=divmod(a,36)
    #ndom_6,rem=divmod(rem,6)
    #ndom_1=rem-1
    #x=(ndom_36)+(ndom_6)+(ndom_1)
    #y=str(x)
    #ndom=eval(y)
    
    #return(ndom)
    
#decimal_to_ndom(1)

def ndom_add(a,b):     

   # a,b=eval(input("first:")),eval(input("second:"))
    dec_add=ndom_to_decimal(a)+ndom_to_decimal(b)
    ndom_add=decimal_to_ndom(dec_add)
    
    return(ndom_add)
    
#ndom_add(1,1)
    
def ndom_multiply (a, b):
    #a,b=eval(input("first:")),eval(input("second:"))
    dec_mult=ndom_to_decimal (a)*ndom_to_decimal (b)
    ndom_mult=decimal_to_ndom(dec_mult)
        
    return(ndom_mult)    
    
#print(ndom_multiply(1,1))