#Shahrain Coovadia 
#CVDSHA002
#import


def get_integer (n):                    #define method
      
   if n=="n":
      n = input ("Enter n:\n")             #for n permutation       
      while not n.isdigit (): 
         n = input ("Enter n:\n")
      n = eval (n)
      return n

   if n=="k":                               #for k permutation
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

def calc_factorial (n):             #for n factorial          
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial   



   

