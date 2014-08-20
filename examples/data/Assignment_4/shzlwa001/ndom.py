''' Definitions of Ndom* functions
    Lwazi Shezi CSC1015F
    03.04.2014'''


def decimal_to_ndom(num):
    
      x =(num//36)
      y =((num-(36*x))//6)
      z=(num%6)
      
      p=str(x) + str(y) + str(z)
      q=int(p)
      return q 
        

def  ndom_to_decimal(ndom):
    y=str(ndom)
    if len(y)==1:
        x=int(y)
    elif len(y)==2:
    
            r=int(y[1])
            k=int(y[0])*6
            x=r+k
    

    else:
            r=int(y[2])
            k=int(y[1])*6        
            j=int(y[0])*36
            x=r+k+j
    return x


def ndom_add(a,b):
    
        a=ndom_to_decimal(a)
        b=ndom_to_decimal(b)
        ans =a+b
        ans =decimal_to_ndom(ans)
        return ans     
     
     
def ndom_multiply(a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    ans=a*b
    ans=decimal_to_ndom(ans)
    return ans