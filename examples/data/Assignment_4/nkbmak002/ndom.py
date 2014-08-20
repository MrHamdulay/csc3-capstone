import math
   

def decimal_to_ndom(num):
     
    A = num//6**2
    a = num%6**2
    
    
    B = a//6**1
    b = a%6**1
    
    C = b//6**0
    
    
    if  A== 0:
        if B == 0:
            return str(C)
        else:
            return str(B)+str(C)
        
    else:
        return str(A)+str(B)+str(C)



def ndom_to_decimal(num):
    
        d = str(num)
        
        if len(d) == 2:
            
        
            
            y = eval(d[0])
            
            z = eval(d[1])
            
           
            Norm = y*(6**1)+z*(6**0)
                      
            return Norm
            
           
        elif len(d) == 3:
            z = int(d[0])
                
            y = int(d[1])
            
            p = int(d[2])   
          
            return z*(6**2)+y*(6**1)+p*(6**0)
                          
           
            
        elif len(d) == 1:
            z = int(d[0])
            
            return z*(6**0)
            



def ndom_add(num1,num2):
    return int(ndom_to_decimal(num1))+int(ndom_to_decimal(num2))


def ndom_multiply(num1,num2):
    return int(decimal_to_ndom(num1))*int(decimal_to_ndom(num2))
    
