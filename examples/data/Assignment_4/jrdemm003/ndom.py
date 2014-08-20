def ndom_to_decimal(a):
    units=0
    tens=0
    hundreds=0
    length=len(str(a))
    y=0
       
    if 0<a<5:
        units=a
           
    if a<=99: 
        tens=a//10
        units=a%10
              
       
    if a>=99:
        hundreds=a//100
        y=a%100
        tens=y//10
        units=y%10   
    ans= hundreds*36+tens*6+units
    return ans  


def decimal_to_ndom(a):
    units=0
    tens=0
    hundreds=0
    length=len(str(a))
    y=0
    
    if 0<a<5:
        units=a
        
    if length==1: 
        tens=a//6
        units=a%6
        
    if length==2 and a<35:
        tens=a//6
        units=a%6        
    
    if length==3 or length==2:
        hundreds=a//36
        y=a%36
        tens=y//6
        units=y%6
        
        
    ans= units+ tens*10+ hundreds*100  
    return ans

def ndom_multiply(a,b):
    ans=0
    x= ndom_to_decimal(a)
    y= ndom_to_decimal(b)
    ans= x*y
    return decimal_to_ndom(ans)

def ndom_add(a,b):
    ans=0
    x= ndom_to_decimal(a)
    y= ndom_to_decimal(b)
    ans= x+y
    return decimal_to_ndom(ans)    

if '__name__'=="__main__":
    
    ndom_to_decimal (100)
    decimal_to_ndom(35)
    ndom_multiply(5,11)
    ndom_add(5,6)
