#Assignment 4 Question 2 
#ndom
#Shaheen Karodia
#KRDSHA003
#2014-04-02
def ndom_to_decimal(a):
   b=0
   Sum=0
   power=len(str(a))-1
   while power >-1:
      y=(6**(power))*(eval(str(a)[b]))
      Sum=Sum+y
      b=b+1
      power=power-1
      
      
   return (Sum)

 
  
def decimal_to_ndom(a): 
   power=4
   hexnum=""
   while power>-1:
      if a%(6**power)==0:
            
            
            hexnum=hexnum+str(int(a/(6**power))) + power*("0")
            break
        
      if a%(6**power)==a:
            power=power-1
        
      elif a%(6**power) >0:
            b=a%(6**power)
            hexnum=hexnum+str(int((a-b)/(6**power)))
            a=b
            power=power-1
   return hexnum

def ndom_add (a,b):
   d=ndom_to_decimal(a)
   e=ndom_to_decimal(b)
   f=d+e 
   g=decimal_to_ndom(f) 
   return (g) 

def ndom_multiply (a,b):
   d=ndom_to_decimal(a)
   e=ndom_to_decimal(b)
   f=d*e 
   g=decimal_to_ndom(f) 
   return (g)   
   


