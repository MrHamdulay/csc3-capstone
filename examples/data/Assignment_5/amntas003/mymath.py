#Tashfia Amin #AMNTAS003 #Due:17 April 2014

#changed combine programme to work when run in question 3
def get_integer(n):
   if n=="n":
      n = input ("Enter n:\n")
      while not n.isdigit():
         n = input ("Enter n:\n")
      n = eval (n)  
   if n=="k":
      n = input ("Enter k:\n")
      while not n.isdigit():
         n = input ("Enter k:\n")
      n = eval (n)  
   return n    #returning value of n instead of printing

def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial    #returning value instead of printing to avoid double printing when called
         