"""question 4: program mymath for importing use purposes
thrianka naidoo
ndxthr005"""

"""question3: program to create functions 
thrianka naidoo
ndxthr005"""

def get_integer(n):           #Get integer function
   
   if n=="n":                 #n value
      n = input ("Enter n:\n")
      
      while not n.isdigit ():
         n = input ("Enter n:\n")

      n = eval (n)   
      return n
   
   if n=="k":                 #k value
      k = input ("Enter k:\n")

      while not k.isdigit ():
         k = input ("Enter k:\n")

      k = eval (k)
      return k
    
    
def calc_factorial(n):       #factorial function
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
      
   return nfactorial
   