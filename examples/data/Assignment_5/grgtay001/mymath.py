"""my math module for question3
tayla george
17 april 2014"""

def get_integer(string):
   if string == "n": #converting a string into a number
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n") 
      n = eval(n)
      return n
   
   if string == "k": #converting a string into a number
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

      
def calc_factorial(integer):   #calculating factorial
   nfactorial = 1
   for i in range (1, integer+1):
      nfactorial *= i
   return nfactorial  