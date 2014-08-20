import math

def ndom_to_decimal (a):
   a=str(a)
   b=6**(len(a)-1)
   dec=0
   for i in a:
      y=eval(i)
      y=y*b
      i=eval(i)
      dec=dec+y
      b=b//6
   return dec

def decimal_to_ndom(a):
   p=(math.log(a))/(math.log(6))
   p=int(p)
   num=p+1
   div=6**(p)
   ndom=''
   x=a
   for i in range(num):
      y=x%div
      number=(x-y)//div
      number=str(number)
      ndom=ndom+number
      x=y
      div=div//6
   ndom=eval(ndom)
   return ndom

def ndom_add(a,b):
   x=ndom_to_decimal(a) + ndom_to_decimal(b)
   y= decimal_to_ndom(x)
   return y

def ndom_multiply(a,b):
   x=(ndom_to_decimal(a)) * (ndom_to_decimal(b))
   y=decimal_to_ndom(x)
   return y
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
        
        
        
        