#GLMSUM001
#Sumayah Goolam Rassool.
# 15 April 2014


#----------------------------------------Function to get integer---------------------------------
def get_integer(n):    
   
   if n=="n": 
      
      n = input ("Enter n:\n")#-------allows for user to input
      
      while not n.isdigit ():#--------reloops 
         
         n = input ("Enter n:\n")
         
      n = eval (n)  
      
      return n
   
   if n=="k": 
      
      k = input ("Enter k:\n")#--------allows for user to input
     
      while not k.isdigit ():#---------reloops 
         
         k = input ("Enter k:\n")
         
      k = eval (k)
      
      return k
    
#-----------------------------------Function to calculate factorial------------------------------

def calc_factorial(n): 
   
   nfactorial = 1#-------------------sets nfactorial to the first factor(1)
   
   for i in range (1,n+1):#---------loop from 1 to n(value of input)
      
      nfactorial *= i#---------------multiplies nfactorial value by i as i increases by 1 each time the loop is executed
      
   return nfactorial#----------------returns the final factorial value
   
