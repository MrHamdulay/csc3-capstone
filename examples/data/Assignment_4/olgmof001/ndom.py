def ndom_to_decimal(a):
        f=a//100
        b=(a%100)//10
        c=(a%100)%10
        return f*36+b*6+c 
    
   
def decimal_to_ndom(a):
        f=a//36
        b=(a%36)//6
        c=(a%36)%6
        return f*100+b*10+c

def ndom_add (a, b):
        x=ndom_to_decimal(a)
        y=ndom_to_decimal(b)
        p=x+y
        q=decimal_to_ndom(p)
        return q

def ndom_multiply (a, b):
        x=ndom_to_decimal(a)
        y=ndom_to_decimal(b)
        p=x*y
        q=decimal_to_ndom(p)
        return q
        
        
 